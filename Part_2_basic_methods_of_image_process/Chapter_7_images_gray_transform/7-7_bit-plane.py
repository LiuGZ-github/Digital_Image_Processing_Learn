import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def bit_plane():
    gray = cv.imread("../../statics/images/Fig0703.png", flags=0)
    height, width = gray.shape[:2]

    bitLayer = np.zeros((8, height, width), np.uint8)
    for i in range(8):
        bitLayer[i] = cv.bitwise_and(gray, int(np.power(2, i)))

    plt.figure(figsize=(9, 8))
    plt.subplot(331), plt.axis("off"), plt.title("1. original")
    plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
    for i in range(8):
        plt.subplot(3, 3, 9 - i), plt.axis("off"), plt.title("{}".format(9 - i - 1))

        plt.imshow(bitLayer[i], cmap="gray", vmin=0, vmax=255)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    bit_plane()