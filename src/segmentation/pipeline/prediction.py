import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

from segmentation.constants import *
from segmentation.utils.common import read_yaml


class Prediction:
    def __init__(self, background_filepath, config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        self.background_filepath = background_filepath
        self.width, self.height, self.channels = self.params.IMAGE_SIZE
        self.model_path = r"E:\jupyter\image segmentation\Project2\segmentation_VB.hdf5"  # self.config.training.trained_model_path
        self.model = load_model(self.model_path)

    def preprocessing(self, image):
        pil_img = Image.fromarray(image)
        frame_resize = pil_img.resize((self.width, self.height), Image.LANCZOS)
        frame = np.array(frame_resize)
        frame = np.expand_dims(frame, axis=0)

        return frame

    def overlap(self, image, mask):
        overlapped = []
        shape = image.shape
        for i in range(shape[0]):
            l1 = []
            for j in range(shape[1]):
                tem = image[i][j] * int(mask[i][j])
                l1.append(tem)
            overlapped.append(l1)

        result = np.array(overlapped)
        return result

    def overlap_with_background(self, image):
        bac = plt.imread(r"{}".format(self.background_filepath))
        bac = Image.fromarray(bac)
        bac = bac.resize((self.width, self.height), Image.LANCZOS)
        bac = np.array(bac)
        overlapped = []
        shape = image.shape
        for i in range(shape[0]):
            l1 = []
            for j in range(shape[1]):
                if np.all(image[i][j] == 0):
                    tem = bac[i][j]
                else:
                    tem = image[i][j]
                l1.append(tem)
            overlapped.append(l1)

        result = np.array(overlapped)
        return result

    def predict(self, image):
        image = self.preprocessing(image)
        predicted_mask = self.model.predict(image)
        predicted_mask = np.round(predicted_mask, decimals=1)
        image = self.overlap(image[0], predicted_mask[0])
        final_image = self.overlap_with_background(image)
        pil_img = Image.fromarray(final_image)
        frame_resize = pil_img.resize((640, 480), Image.LANCZOS)
        final_image = np.array(frame_resize)
        return final_image


if __name__ == '__main__':
    import cv2

    back_ground = r"D:\Desktop\O1.jpg"
    process = Prediction(back_ground)
    cap = cv2.VideoCapture(0)
    while True:
        score, img = cap.read()
        img = cv2.flip(img, 1)
        img = process.predict(img)
        if cv2.waitKey(1) == ord("q"):
            break
        cv2.imshow("CAM1", img)
    cap.release()
    cv2.destroyAllWindows()
