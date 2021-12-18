import os
import random

import cv2.cv2 as cv2
import numpy as np


def remove_small_pictures():
    parent = "data/getchu/"
    files = os.listdir(parent)
    n = 0
    for file in files:
        image = cv2.imread(parent+file)
        if image.shape[0] < 92 or image.shape[1] < 92:
            os.remove(parent+file)
            n += 1
    print(n)


def increase_resolution_getchu():
    parent = "data/getchu/"
    parent_v2 = "data/getchu-v2/"
    files = os.listdir(parent)
    os.mkdir(parent_v2)
    for file in files:
        image = cv2.imread(parent+file)
        image = cv2.resize(image, (256, 256))
        cv2.imwrite(parent_v2+file, image)


def increase_resolution_celeba():
    parent = "data/test/"
    parent_v2 = "data/test-v2/"
    files = os.listdir(parent)
    os.mkdir(parent_v2)
    for file in files:
        image = cv2.imread(parent+file)
        if image.shape[0] > image.shape[1]:
            mid = (image.shape[0]-image.shape[1])//2
            image = image[mid:mid+image.shape[1], :]
        elif image.shape[1] > image.shape[0]:
            mid = (image.shape[1] - image.shape[0]) / 2
            image = image[:, mid:mid + image.shape[0]]
        image = cv2.resize(image, (256, 256))
        cv2.imwrite(parent_v2+file, image)


def arrange_data_correctly(folder):
    parent = f"data/{folder}/"
    parent_v2 = f"data/{folder}-v2/"
    files = os.listdir(parent)
    os.mkdir(parent_v2)
    n = 0
    for file in files:
        n += 1
        if n % 100 == 0:
            print(n)
        image = cv2.imread(parent + file)
        if image.shape[0] > image.shape[1]:
            mid = random.randint(0, (image.shape[0] - image.shape[1]))
            image = image[mid:mid + image.shape[1], :]
        elif image.shape[1] > image.shape[0]:
            mid = random.randint(0, (image.shape[1] - image.shape[0]))
            image = image[:, mid:mid + image.shape[0]]
        image = cv2.resize(image, (256, 256))
        cv2.imwrite(parent_v2+file, image)
