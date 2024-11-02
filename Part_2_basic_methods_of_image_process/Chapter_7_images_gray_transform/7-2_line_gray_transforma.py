import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def line_gray_transform():
    gray = cv.imread("../../statics/images/Lena.tif", flags=0)
    h, w = gray.shape[:2]

    # 线性变换参数 dst = a * src + b
    a1, b1 = 1, 100  # 灰度值上移
    a2, b2 = 1, -100  # 灰度值下移
    a3, b3 = 3, 0  # 对比度增强
    a4, b4 = 0.1, 0  # 对比度减弱
    a5, b5 = -0.1, 0  #暗区域变亮， 亮区域变暗
    a6, b6 = -1, 255  # 灰度值反转

    # 灰度线性变换
    timeBegin = cv.getTickCount()
    img1 = cv.convertScaleAbs(gray, alpha=a1, beta=b1)
    img2 = cv.convertScaleAbs(gray, alpha=a2, beta=b2)
    img3 = cv.convertScaleAbs(gray, alpha=a3, beta=b3)
    img4 = cv.convertScaleAbs(gray, alpha=a4, beta=b4)
    img5 = cv.convertScaleAbs(gray, alpha=a5, beta=b5)
    img6 = cv.convertScaleAbs(gray, alpha=a6, beta=b6)
    timeEnd = cv.getTickCount()
    print((timeEnd - timeBegin) / cv.getTickFrequency())

    imgList = [img1, img2, img3, img4, img5, img6]
    plt.figure(figsize=(9, 6))
    for i in range(0, len(imgList)):
        plt.subplot(2, 3, i + 1),plt.title("{}".format(i + 1))
        plt.axis('off'), plt.imshow(imgList[i], cmap='gray')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    line_gray_transform()