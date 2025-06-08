from segmentation.config.configuration import EvaluationConfig
import tensorflow as tf
from pathlib import Path
from segmentation.utils.common import save_json


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.model = None
        self.score = None
        self.config = config

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self, X, Y):
        self.model = self.load_model(self.config.path_of_model)

        self.score = self.model.evaluate(X[:100], Y[:100])

    def save_score(self, file_path):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=file_path, data=scores)
