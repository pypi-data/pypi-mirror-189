import abc

from ..data.data_generator import DataGenFeat, DataGenPure, DataGenSequence


class BaseTrainer(abc.ABC):
    def __init__(
        self,
        model,
        task,
        loss_type,
        n_epochs,
        lr,
        lr_decay,
        epsilon,
        batch_size,
        num_neg,
    ):
        self.model = model
        self.task = task
        self.loss_type = loss_type
        self.n_epochs = n_epochs
        self.lr = lr
        self.lr_decay = lr_decay
        self.epsilon = epsilon
        self.batch_size = batch_size
        self.num_neg = num_neg

    def get_data_generator(self, train_data):
        if self.model.model_category == "pure":
            data_generator = DataGenPure(train_data)
        elif self.model.model_category == "feat":
            data_generator = DataGenFeat(
                train_data, self.model.sparse, self.model.dense
            )
        else:
            data_generator = DataGenSequence(
                train_data,
                self.model.data_info,
                self.model.sparse if hasattr(self.model, "sparse") else False,
                self.model.dense if hasattr(self.model, "dense") else False,
                self.model.interaction_mode,
                self.model.max_seq_len,
                self.model.n_items,
            )
        return data_generator

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        raise NotImplementedError
