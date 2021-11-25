import pandas as pd
import numpy as np
import os
import cv2
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

plt.figure(figsize=(20, 20))

root = os.path.dirname(__file__)

parentPath = root[:root.rfind('\\')] + '\\dataset_generator\\frames'
print(parentPath)


# only takes a couple of images for testing from the first movie
def test_image_plotting():
    for movie in os.listdir(parentPath):
        count = 0
        for image in os.listdir(f'{parentPath}\\{movie}'):
            image_path = f'{parentPath}\\{movie}\\{image}'
            print(image_path)
            img = mpimg.imread(image_path)
            ax = plt.subplot(1, 5, count + 1)
            ax.title.set_text(image)
            plt.imshow(img)
            count += 1
            if count == 5:
                break
        plt.show()
        break


def create_dataset():
    img_data_array = []
    for movie in os.listdir(parentPath):
        for image in os.listdir(f'{parentPath}\\{movie}'):
            image_path = f'{parentPath}\\{movie}\\{image}'
            print(image_path)

            img = np.array(Image.open(image_path))
            img = np.resize(img, (256, 256, 3))
            img = img.astype('float32')
            img /= 255
            img_data_array.append(img)
        break
    return img_data_array


print(create_dataset())
