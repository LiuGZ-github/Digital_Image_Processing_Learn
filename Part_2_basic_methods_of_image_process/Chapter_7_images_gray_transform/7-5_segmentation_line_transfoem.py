import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize


def segmentation_line_transform():
    gray = cv.imread("../../statics/images/Fig0703.png", flags=0)

    # 拉伸控制点
    r1, s1 = 128, 64
    r2, s2 = 192, 224

    # LUT 函数快速查表法实现对比度拉伸
    luTable = np.zeros(256)
    for i in range(256):
        if i < r1:
            luTable[i] = (s1 / r1) * i
        elif i < r2:
            luTable[i] = ((s2 - s1) / (r2 - r1)) * (i - r1) + s1
        else:
            luTable[i] = ((s2 - 255.0) / (r2 - 255.0)) * (i - s2) + s2
    imgSLT = np.uint8(cv.LUT(gray, luTable))

    plt.figure(figsize=(12, 8))
    plt.subplot(121), plt.title("1. original"), plt.axis("off")
    plt.imshow(gray, cmap="gray", vmin=0, vmax=255)

    plt.subplot(122), plt.title("2. LUT"), plt.axis("off")
    plt.imshow(imgSLT, cmap="gray", vmin=0, vmax=255)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    segmentation_line_transform()