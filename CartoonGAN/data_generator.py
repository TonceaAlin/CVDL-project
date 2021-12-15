import os
import random

import cv2.cv2 as cv2
import numpy as np
import tensorflow as tf


def crop_image(image):
    if image.shape[0] == image.shape[1]:
        return image
    if image.shape[0] > image.shape[1]:
        start = random.randint(0, image.shape[0]-image.shape[1])
        return image[start:start+image.shape[1], :]
    start = random.randint(0, image.shape[1] - image.shape[0])
    return image[:, start:start + image.shape[0]]


def resize_image(image, shape):
    image = crop_image(image)
    return cv2.resize(image, shape)


def get_photos_from_folder(folder, input_size):
    photos = []
    for file in os.listdir(folder):
        image = cv2.imread(folder + "/" + file)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = resize_image(image, input_size).astype(np.float32)
        photos.append(image)
    return np.asarray(photos)
