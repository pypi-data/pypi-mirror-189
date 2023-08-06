"""

Reference: Balazs Hidasi et al.  "Session-based Recommendations with Recurrent Neural Networks"
           (https://arxiv.org/pdf/1511.06939.pdf)

author: massquantity

"""
import numpy as np
from tensorflow.keras.initializers import glorot_normal as tf_glorot_normal
from tensorflow.keras.initializers import truncated_normal as tf_truncated_normal
from tensorflow.keras.initializers import zeros as tf_zeros

from ..bases import EmbedBase, ModelMeta
from ..data.sequence import get_user_last_interacted
from ..tfops import dropout_config, reg_config, sess_config, tf, tf_dense, tf_rnn
from ..training import RNN4RecTrainer
from ..utils.misc import count_params
from ..utils.validate import check_interaction_mode


class RNN4Rec(EmbedBase, metaclass=ModelMeta, backend="tensorflow"):
    item_variables = ["item_weights", "item_biases", "input_embed"]

    def __init__(
        self,
        task,
        data_info=None,
        loss_type="cross_entropy",
        rnn_type="lstm",
        embed_size=16,
        n_epochs=20,
        lr=0.001,
        lr_decay=False,
        epsilon=1e-5,
        hidden_units="16",
        reg=None,
        batch_size=256,
        num_neg=1,
        dropout_rate=None,
        use_layer_norm=False,
        recent_num=10,
        random_num=None,
        seed=42,
        lower_upper_bound=None,
        tf_sess_config=None,
        with_training=True,
    ):
        super().__init__(task, data_info, embed_size, lower_upper_bound)

        self.all_args = locals()
        self.rnn_type = rnn_type.lower()
        self.hidden_units = list(map(int, hidden_units.split(",")))
        self.reg = reg_config(reg)
        self.dropout_rate = dropout_config(dropout_rate)
        self.use_ln = use_layer_norm
        self.seed = seed
        (self.interaction_mode, self.max_seq_len) = check_interaction_mode(
            recent_num, random_num
        )
        (
            self.user_last_interacted,
            self.last_interacted_len,
        ) = self._set_last_interacted()
        self._check_params()
        if with_training:
            self._build_model(loss_type)
            self.sess = sess_config(tf_sess_config)
            self.trainer = RNN4RecTrainer(
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

    def _build_model(self, loss_type):
        tf.set_random_seed(self.seed)
        self.labels = tf.placeholder(tf.float32, shape=[None])
        self.is_training = tf.placeholder_with_default(False, shape=[])
        self._build_variables()
        self._build_user_embeddings()
        if self.task == "rating" or loss_type in ("cross_entropy", "focal"):
            self.user_indices = tf.placeholder(tf.int32, shape=[None])
            self.item_indices = tf.placeholder(tf.int32, shape=[None])

            item_vector = tf.nn.embedding_lookup(self.item_weights, self.item_indices)
            item_bias = tf.nn.embedding_lookup(self.item_biases, self.item_indices)
            self.output = (
                tf.reduce_sum(tf.multiply(self.user_vector, item_vector), axis=1)
                + item_bias
            )

        elif loss_type == "bpr":
            self.item_indices_pos = tf.placeholder(tf.int32, shape=[None])
            self.item_indices_neg = tf.placeholder(tf.int32, shape=[None])
            item_embed_pos = tf.nn.embedding_lookup(
                self.item_weights, self.item_indices_pos
            )
            item_embed_neg = tf.nn.embedding_lookup(
                self.item_weights, self.item_indices_neg
            )
            item_bias_pos = tf.nn.embedding_lookup(
                self.item_biases, self.item_indices_pos
            )
            item_bias_neg = tf.nn.embedding_lookup(
                self.item_biases, self.item_indices_neg
            )

            item_diff = tf.subtract(item_bias_pos, item_bias_neg) + tf.reduce_sum(
                tf.multiply(
                    self.user_vector, tf.subtract(item_embed_pos, item_embed_neg)
                ),
                axis=1,
            )
            self.bpr_loss = tf.log_sigmoid(item_diff)

        count_params()

    def _build_variables(self):
        # weight and bias parameters for last fc_layer
        self.item_biases = tf.get_variable(
            name="item_biases",
            shape=[self.n_items],
            initializer=tf_zeros,
            regularizer=self.reg,
        )
        self.item_weights = tf.get_variable(
            name="item_weights",
            shape=[self.n_items, self.embed_size],
            initializer=tf_truncated_normal(0.0, 0.02),
            regularizer=self.reg,
        )

        # input_embed for rnn_layer, include padding value
        self.input_embed = tf.get_variable(
            name="input_embed",
            shape=[self.n_items + 1, self.hidden_units[0]],
            initializer=tf_glorot_normal,
            regularizer=self.reg,
        )

    def _build_user_embeddings(self):
        self.user_interacted_seq = tf.placeholder(
            tf.int32, shape=[None, self.max_seq_len]
        )
        self.user_interacted_len = tf.placeholder(tf.int64, shape=[None])
        seq_item_embed = tf.nn.embedding_lookup(
            self.input_embed, self.user_interacted_seq
        )
        rnn_output = tf_rnn(
            inputs=seq_item_embed,
            rnn_type=self.rnn_type,
            lengths=self.user_interacted_len,
            maxlen=self.max_seq_len,
            hidden_units=self.hidden_units,
            dropout_rate=self.dropout_rate,
            use_ln=self.use_ln,
            is_training=self.is_training,
        )
        self.user_vector = tf_dense(units=self.embed_size, activation=None)(rnn_output)

    def _set_last_interacted(self):
        user_last_interacted, last_interacted_len = get_user_last_interacted(
            self.n_users, self.user_consumed, self.n_items, self.max_seq_len
        )
        return user_last_interacted, last_interacted_len.astype(np.int64)

    def set_embeddings(self):
        feed_dict = {
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

    def _check_params(self):
        # assert self.hidden_units[-1] == self.embed_size, (
        #    "dimension of last rnn hidden unit should equal to embed_size"
        # )
        assert self.rnn_type in ("lstm", "gru"), "rnn_type must be either lstm or gru"
