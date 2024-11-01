import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def gray_level_layer():
    gray = cv.imread("../../statics/images/Fig0703.png", flags=0)
    width, height = gray.shape[:2]

    # 二值变换灰度级分层
    a, b = 155, 245
    binLayer = gray.copy()
    LUTtable = np.zeros(256)
    for i in range(256):
        if i < a or i > b:
            LUTtable[i] = 0
        else:
            LUTtable[i] = 255
    binLayer = cv.LUT(binLayer, LUTtable)

    # 增强选择的灰度窗口
    winLayer = gray.copy()
    LUTtable = np.zeros(256)
    for i in range(256):
        if a <= i <= b:
            LUTtable[i] = 245
        else:
            LUTtable[i] = i
    winLayer = cv.LUT(winLayer, LUTtable)

    plt.figure(figsize=(9, 3.5))
    plt.subplot(131), plt.axis('off'), plt.title("1. original")
    plt.imshow(gray, cmap='gray')
    plt.subplot(132), plt.axis('off'), plt.title("2. gray level")
    plt.imshow(binLayer, cmap='gray')
    plt.subplot(133), plt.axis('off'), plt.title("3. gray level")
    plt.imshow(winLayer, cmap='gray')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    gray_level_layer()