"""

Reference: Aaron van den Oord et al. "WaveNet: A Generative Model for Raw Audio"
           (https://arxiv.org/pdf/1609.03499.pdf)

author: massquantity

"""
import numpy as np
from tensorflow.keras.initializers import glorot_normal as tf_glorot_normal
from tensorflow.keras.initializers import truncated_normal as tf_truncated_normal
from tensorflow.keras.initializers import zeros as tf_zeros

from ..bases import EmbedBase, ModelMeta
from ..data.sequence import get_user_last_interacted
from ..tfops import (
    conv_nn,
    dropout_config,
    max_pool,
    reg_config,
    sess_config,
    tf,
    tf_dense,
)
from ..training import TensorFlowTrainer
from ..utils.misc import count_params
from ..utils.validate import check_interaction_mode


class WaveNet(EmbedBase, metaclass=ModelMeta, backend="tensorflow"):
    user_variables = ["user_feat"]
    item_variables = ["item_weights", "item_biases", "input_embed"]

    def __init__(
        self,
        task,
        data_info=None,
        loss_type="cross_entropy",
        embed_size=16,
        n_epochs=20,
        lr=0.001,
        lr_decay=False,
        epsilon=1e-5,
        reg=None,
        batch_size=256,
        num_neg=1,
        dropout_rate=None,
        use_bn=False,
        n_filters=16,
        n_blocks=1,
        n_layers_per_block=4,
        recent_num=10,
        random_num=None,
        seed=42,
        lower_upper_bound=None,
        tf_sess_config=None,
        with_training=True,
    ):
        super().__init__(task, data_info, embed_size, lower_upper_bound)

        self.all_args = locals()
        self.reg = reg_config(reg)
        self.dropout_rate = dropout_config(dropout_rate)
        self.use_bn = use_bn
        self.n_filters = n_filters
        self.n_blocks = n_blocks
        self.n_layers_per_block = n_layers_per_block
        self.seed = seed
        (self.interaction_mode, self.max_seq_len) = check_interaction_mode(
            recent_num, random_num
        )
        (
            self.user_last_interacted,
            self.last_interacted_len,
        ) = self._set_last_interacted()
        if with_training:
            self._build_model()
            self.sess = sess_config(tf_sess_config)
            self.trainer = TensorFlowTrainer(
                self,
                task,
                loss_type,
                n_epochs,
                lr,
                lr_decay,
                epsilon,
                batch_size,
                num_neg,
            )

    def _build_model(self):
        tf.set_random_seed(self.seed)
        self._build_placeholders()
        self._build_variables()
        self._build_user_embeddings()

        item_vector = tf.nn.embedding_lookup(self.item_weights, self.item_indices)
        item_bias = tf.nn.embedding_lookup(self.item_biases, self.item_indices)
        self.output = (
            tf.reduce_sum(tf.multiply(self.user_vector, item_vector), axis=1)
            + item_bias
        )
        count_params()

    def _build_placeholders(self):
        self.user_indices = tf.placeholder(tf.int32, shape=[None])
        self.item_indices = tf.placeholder(tf.int32, shape=[None])
        self.user_interacted_seq = tf.placeholder(
            tf.int32, shape=[None, self.max_seq_len]
        )
        self.user_interacted_len = tf.placeholder(tf.int64, shape=[None])
        self.labels = tf.placeholder(tf.float32, shape=[None])
        self.is_training = tf.placeholder_with_default(False, shape=[])

    def _build_variables(self):
        self.user_feat = tf.get_variable(
            name="user_feat",
            shape=[self.n_users, self.embed_size],
            initializer=tf_truncated_normal(0.0, 0.01),
            regularizer=self.reg,
        )

        # weight and bias parameters for last fc_layer
        self.item_biases = tf.get_variable(
            name="item_biases",
            shape=[self.n_items],
            initializer=tf_zeros,
        )
        self.item_weights = tf.get_variable(
            name="item_weights",
            shape=[self.n_items, self.embed_size * 2],
            initializer=tf_truncated_normal(0.0, 0.02),
            regularizer=self.reg,
        )

        # input_embed for cnn_layer, include padding value
        self.input_embed = tf.get_variable(
            name="input_embed",
            shape=[self.n_items + 1, self.embed_size],
            initializer=tf_glorot_normal,
            regularizer=self.reg,
        )

    def _build_user_embeddings(self):
        user_repr = tf.nn.embedding_lookup(self.user_feat, self.user_indices)
        # B * seq * K
        seq_item_embed = tf.nn.embedding_lookup(
            self.input_embed, self.user_interacted_seq
        )

        convs_out = seq_item_embed
        for _ in range(self.n_blocks):
            for i in range(self.n_layers_per_block):
                convs_out = conv_nn(
                    filters=self.n_filters,
                    kernel_size=2,
                    strides=1,
                    padding="causal",
                    activation=tf.nn.relu,
                    dilation_rate=2**i,
                )(inputs=convs_out)

        convs_out = conv_nn(
            filters=self.n_filters,
            kernel_size=1,
            strides=1,
            padding="valid",
            activation=tf.nn.relu,
        )(inputs=convs_out)

        # convs_out = tf.layers.flatten(convs_out)
        p_size = convs_out.get_shape().as_list()[1]
        convs_out = max_pool(pool_size=p_size, strides=1, padding="valid")(
            inputs=convs_out
        )

        convs_out = tf.squeeze(convs_out, axis=1)
        convs_out = tf_dense(units=self.embed_size, activation=None)(convs_out)
        self.user_vector = tf.concat([user_repr, convs_out], axis=1)

    def _set_last_interacted(self):
        user_last_interacted, last_interacted_len = get_user_last_interacted(
            self.n_users, self.user_consumed, self.n_items, self.max_seq_len
        )
        return user_last_interacted, last_interacted_len.astype(np.int64)

    def set_embeddings(self):
        feed_dict = {
            self.user_indices: np.arange(self.n_users),
            self.user_interacted_seq: self.user_last_interacted,
            self.user_interacted_len: self.last_interacted_len,
        }
        user_vector = self.sess.run(self.user_vector, feed_dict)
        item_weights = self.sess.run(self.item_weights)
        item_biases = self.sess.run(self.item_biases)

        user_bias = np.ones([len(user_vector), 1], dtype=user_vector.dtype)
        item_bias = item_biases[:, None]
        self.user_embed = np.hstack([user_vector, user_bias])
        self.item_embed = np.hstack([item_weights, item_bias])
