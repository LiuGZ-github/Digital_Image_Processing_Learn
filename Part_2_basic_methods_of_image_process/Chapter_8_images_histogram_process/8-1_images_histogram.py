import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def image_histogram():
    img = cv.imread("../../statics/images/Lena.tif", flags=1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    histCV = cv.calcHist([gray], [0], None, [256], [0, 256])

    histNP, bins = np.histogram(gray.flatten(), 256)

    print(histCV.shape, histNP.shape)
    print(histCV.max(), histNP.max())
    plt.figure(figsize=(9, 3))
    plt.subplot(131, yticks=[]), plt.axis((0., 255., 0., float(np.max(histNP))))
    plt.title("1. Gray hist (np)")
    plt.bar(range(256), histNP[:])

    plt.subplot(132, yticks=[]), plt.axis((0., 255., 0., float(np.max(histCV))))
    plt.title("2. cv")
    plt.bar(range(256), histCV[:, 0])

    plt.subplot(133, yticks=[])
    plt.title("3. Color histogram")
    color = ['b', 'r', 'g']
    for ch, col in enumerate(color):
        histCh = cv.calcHist([img], [ch], None, [256], [0, 256])
        plt.plot(histCh[:, 0], color=col)
        plt.xlim([0, 256])

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    image_histogram()