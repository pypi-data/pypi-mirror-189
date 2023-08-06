"""

Reference: Paul Covington et al.  "Deep Neural Networks for YouTube Recommendations"
           (https://static.googleusercontent.com/media/research.google.com/zh-CN//pubs/archive/45530.pdf)

author: massquantity

"""
import numpy as np
from tensorflow.keras.initializers import truncated_normal as tf_truncated_normal

from ..bases import ModelMeta, TfBase
from ..data.sequence import get_user_last_interacted
from ..tfops import (
    dense_nn,
    dropout_config,
    multi_sparse_combine_embedding,
    reg_config,
    tf,
    tf_dense,
)
from ..training import TensorFlowTrainer
from ..utils.misc import count_params
from ..utils.validate import (
    check_dense_values,
    check_interaction_mode,
    check_multi_sparse,
    check_sparse_indices,
    dense_field_size,
    sparse_feat_size,
    sparse_field_size,
    true_sparse_field_size,
)


class YouTubeRanking(TfBase, metaclass=ModelMeta):
    """
    The model implemented mainly corresponds to the ranking phase
    based on the original paper.
    """

    user_variables = ["user_features"]
    item_variables = ["item_features"]
    sparse_variables = ["sparse_features"]
    dense_variables = ["dense_features"]

    def __init__(
        self,
        task="ranking",
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
        use_bn=True,
        dropout_rate=None,
        hidden_units="128,64,32",
        recent_num=10,
        random_num=None,
        multi_sparse_combiner="sqrtn",
        seed=42,
        lower_upper_bound=None,
        tf_sess_config=None,
        with_training=True,
    ):
        super().__init__(task, data_info, lower_upper_bound, tf_sess_config)

        assert task == "ranking", "YouTube models is only suitable for ranking"
        self.all_args = locals()
        self.embed_size = embed_size
        self.reg = reg_config(reg)
        self.use_bn = use_bn
        self.dropout_rate = dropout_config(dropout_rate)
        self.hidden_units = list(map(int, hidden_units.split(",")))
        self.interaction_mode, self.max_seq_len = check_interaction_mode(
            recent_num, random_num
        )
        self.seed = seed
        self.sparse = check_sparse_indices(data_info)
        self.dense = check_dense_values(data_info)
        if self.sparse:
            self.sparse_feature_size = sparse_feat_size(data_info)
            self.sparse_field_size = sparse_field_size(data_info)
            self.multi_sparse_combiner = check_multi_sparse(
                data_info, multi_sparse_combiner
            )
            self.true_sparse_field_size = true_sparse_field_size(
                data_info, self.sparse_field_size, self.multi_sparse_combiner
            )
        if self.dense:
            self.dense_field_size = dense_field_size(data_info)
        (
            self.user_last_interacted,
            self.last_interacted_len,
        ) = self._set_last_interacted()
        self._build_model()
        if with_training:
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
        self.user_indices = tf.placeholder(tf.int32, shape=[None])
        self.item_indices = tf.placeholder(tf.int32, shape=[None])
        self.user_interacted_seq = tf.placeholder(
            tf.int32, shape=[None, self.max_seq_len]
        )
        self.user_interacted_len = tf.placeholder(tf.float32, shape=[None])
        self.labels = tf.placeholder(tf.float32, shape=[None])
        self.is_training = tf.placeholder_with_default(False, shape=[])
        self.concat_embed = []

        user_features = tf.get_variable(
            name="user_features",
            shape=[self.n_users + 1, self.embed_size],
            initializer=tf_truncated_normal(0.0, 0.01),
            regularizer=self.reg,
        )
        item_features = tf.get_variable(
            name="item_features",
            shape=[self.n_items + 1, self.embed_size],
            initializer=tf_truncated_normal(0.0, 0.01),
            regularizer=self.reg,
        )
        user_embed = tf.nn.embedding_lookup(user_features, self.user_indices)
        item_embed = tf.nn.embedding_lookup(item_features, self.item_indices)

        # unknown items are padded to 0-vector
        zero_padding_op = tf.scatter_update(
            item_features, self.n_items, tf.zeros([self.embed_size], dtype=tf.float32)
        )
        with tf.control_dependencies([zero_padding_op]):
            # B * seq * K
            multi_item_embed = tf.nn.embedding_lookup(
                item_features, self.user_interacted_seq
            )
        pooled_embed = tf.div_no_nan(
            tf.reduce_sum(multi_item_embed, axis=1),
            tf.expand_dims(tf.sqrt(self.user_interacted_len), axis=1),
        )
        self.concat_embed.extend([user_embed, item_embed, pooled_embed])

        if self.sparse:
            self._build_sparse()
        if self.dense:
            self._build_dense()

        concat_embed = tf.concat(self.concat_embed, axis=1)
        mlp_layer = dense_nn(
            concat_embed,
            self.hidden_units,
            use_bn=self.use_bn,
            dropout_rate=self.dropout_rate,
            is_training=self.is_training,
        )
        self.output = tf.reshape(tf_dense(units=1)(mlp_layer), [-1])
        count_params()

    def _build_sparse(self):
        self.sparse_indices = tf.placeholder(
            tf.int32, shape=[None, self.sparse_field_size]
        )
        sparse_features = tf.get_variable(
            name="sparse_features",
            shape=[self.sparse_feature_size, self.embed_size],
            initializer=tf_truncated_normal(0.0, 0.01),
            regularizer=self.reg,
        )

        if self.data_info.multi_sparse_combine_info and self.multi_sparse_combiner in (
            "sum",
            "mean",
            "sqrtn",
        ):
            sparse_embed = multi_sparse_combine_embedding(
                self.data_info,
                sparse_features,
                self.sparse_indices,
                self.multi_sparse_combiner,
                self.embed_size,
            )
        else:
            sparse_embed = tf.nn.embedding_lookup(sparse_features, self.sparse_indices)

        sparse_embed = tf.reshape(
            sparse_embed, [-1, self.true_sparse_field_size * self.embed_size]
        )
        self.concat_embed.append(sparse_embed)

    def _build_dense(self):
        self.dense_values = tf.placeholder(
            tf.float32, shape=[None, self.dense_field_size]
        )
        dense_values_reshape = tf.reshape(
            self.dense_values, [-1, self.dense_field_size, 1]
        )
        batch_size = tf.shape(self.dense_values)[0]

        dense_features = tf.get_variable(
            name="dense_features",
            shape=[self.dense_field_size, self.embed_size],
            initializer=tf_truncated_normal(0.0, 0.01),
            regularizer=self.reg,
        )

        dense_embed = tf.tile(dense_features, [batch_size, 1])
        dense_embed = tf.reshape(
            dense_embed, [-1, self.dense_field_size, self.embed_size]
        )
        dense_embed = tf.multiply(dense_embed, dense_values_reshape)
        dense_embed = tf.reshape(
            dense_embed, [-1, self.dense_field_size * self.embed_size]
        )
        self.concat_embed.append(dense_embed)

    def _set_last_interacted(self):
        user_last_interacted, last_interacted_len = get_user_last_interacted(
            self.n_users, self.user_consumed, self.n_items, self.max_seq_len
        )
        oov = np.full(self.max_seq_len, self.n_items, dtype=np.int32)
        user_last_interacted = np.vstack([user_last_interacted, oov])
        last_interacted_len = np.append(last_interacted_len, [1])
        return user_last_interacted, last_interacted_len
