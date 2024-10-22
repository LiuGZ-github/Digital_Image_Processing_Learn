import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from numpy.ma.core import subtract


def images_LUT():
    filepath = "../../statics/images/Lena.tif"
    img = cv.imread(filepath, flags=1)
    h, w, ch = img.shape

    timeBegin = cv.getTickCount()
    imgInv = np.empty((w, h, ch), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            for k in range(ch):
                imgInv[i][j][k] = 255 - img[i][j][k]
    timeEnd = cv.getTickCount()
    time = (timeEnd - timeBegin) / cv.getTickFrequency()
    print(time)

    timeBegin = cv.getTickCount()
    transTable = np.array([(255 - i) for i in range(256)]).astype(np.uint8)
    intLUT = cv.LUT(img, transTable)
    timeEnd = cv.getTickCount()
    time = (timeEnd - timeBegin) / cv.getTickFrequency()
    print(time)

    timeBegin = cv.getTickCount()
    subtract = 255 - img
    timeEnd = cv.getTickCount()
    time = (timeEnd - timeBegin) / cv.getTickFrequency()
    print(time)

def images_color_reduce():
    filepath = "../../statics/images/Lena.tif"
    gray = cv.imread(filepath, flags=0)
    h, w = gray.shape[:2]

    timeBegin = cv.getTickCount()
    imgGray32 = np.empty((w, h), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            imgGray32[i][j] = (gray[i][j]) // 8 * 8
    timeEnd = cv.getTickCount()
    time = (timeEnd - timeBegin) / cv.getTickFrequency()
    print(time)

    timeBegin = cv.getTickCount()
    table32 = np.array([(i // 8) * 8 for i in range(256)]).astype(np.uint8)
    gray32 = cv.LUT(gray, table32)
    timeEnd = cv.getTickCount()
    time = (timeEnd - timeBegin) / cv.getTickFrequency()
    print(time)

    table8 = np.array([(i // 32) * 32 for i in range(256)]).astype(np.uint8)
    gray8 = cv.LUT(gray, table8)

    plt.figure(figsize=(9, 3.5))
    plt.subplot(131), plt.title("1.Gray-256"),plt.axis('off')
    plt.imshow(gray,cmap='gray')

    plt.subplot(132), plt.title("2.Gray-32"),plt.axis('off')
    plt.imshow(gray32,cmap='gray')

    plt.subplot(133), plt.title("3.Gray-8"),plt.axis('off')
    plt.imshow(gray8,cmap='gray')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # images_LUT()
    images_color_reduce()