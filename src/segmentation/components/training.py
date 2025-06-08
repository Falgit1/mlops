import tensorflow as tf
import numpy as np
import pandas as pd
from tqdm import tqdm
from PIL import Image
from pathlib import Path
from segmentation import logger
from segmentation.config.configuration import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig):
        self.model = None
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def load_data(self, df, data="train"):
        width, height, channels = self.config.params_image_size

        if data == "train":
            path = "images"
            count = df[path].count()
            train = np.zeros((count, width, height, 3), dtype=np.uint8)

        else:
            path = "masks"
            count = df[path].count()
            train = np.zeros((count, width, height), dtype=np.uint8)

        for i in tqdm(range(count)):
            path1 = f"{self.config.data_path}/data/{df[path][i]}"
            img = Image.open(path1)
            img = img.resize((width, height), Image.LANCZOS)
            try:
                train[i] = np.array(img)
            except Exception as e:
                logger.exception(f"data loading and preprocessing {e}")
        return train

    def data_preprocessing(self):
        df = pd.read_csv(f"{self.config.data_path}/data/train.csv")

        # X data load
        X_train = np.array(self.load_data(df))

        # Y data load
        Y_train = np.array(self.load_data(df, "test"))
        Y_train = np.expand_dims(Y_train, axis=3)
        Y_train = np.array(Y_train, dtype=np.bool_)

        return X_train, Y_train

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    # X_train, Y_train, validation_split=0.1, batch_size=16, epochs=25, callbacks=callbacks

    def train(self, X_train, Y_train, callback_list: list):
        # self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        # self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(X_train, Y_train,
                       epochs=self.config.params_epochs,
                       validation_split=self.config.params_v_split,
                       batch_size=self.config.params_batch_size,
                       callbacks=callback_list
                       )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
