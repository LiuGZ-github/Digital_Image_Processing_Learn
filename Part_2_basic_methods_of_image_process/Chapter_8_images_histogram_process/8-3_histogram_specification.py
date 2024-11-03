import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import yticks


def histogram_specification():
    graySrc = cv.imread("../../statics/images/Fig0702.png", flags=0)
    grayRef = cv.imread("../../statics/images/Fig0701.png", flags=0)

    # 计算累计直方图
    histSrc = cv.calcHist([graySrc], [0], None, [256], [0, 255])  # (256,1)
    histRef = cv.calcHist([grayRef], [0], None, [256], [0, 255])  # (256,1)
    cdfSrc = np.cumsum(histSrc)  # 原始图像累积分布函数 CDF
    cdfRef = np.cumsum(histRef)  # 匹配模板累积分布函数 CDF
    cdfSrc = cdfSrc / cdfSrc[-1]  # 归一化: 0~1
    cdfRef = cdfRef / cdfRef[-1]

    # 计算直方图匹配转换函数
    transMat = np.zeros(256)  # 直方图匹配转换函数
    for i in range(256):
        index = 1
        vMin = abs(cdfSrc[i] - cdfRef[0])
        for j in range(256):
            diff = abs(cdfSrc[i] - cdfRef[j])
            if diff < vMin:
                index = int(j)
                vMin = diff
        transMat[i] = index

    # LUT 实现直方图匹配
    luTable = transMat.astype(np.uint8)
    grayDst = cv.LUT(graySrc, luTable)

    plt.figure(figsize=(9, 6))

    plt.subplot(231), plt.title("1. original"), plt.axis('off')
    plt.imshow(graySrc, cmap='gray')

    plt.subplot(232), plt.title("2. Matching image"), plt.axis('off')
    plt.imshow(grayRef, cmap='gray')

    plt.subplot(233), plt.title("3. Match result"), plt.axis('off')
    plt.imshow(grayDst, cmap='gray')

    plt.subplot(234, xticks=[], yticks=[])
    plt.title("4. origin histogram")
    plt.bar(range(256), histSrc[:, 0])
    plt.axis((0, 255, 0, np.max(histSrc)))

    plt.subplot(235, xticks=[], yticks=[])
    plt.title("4. Matching image histogram")
    plt.bar(range(256), histRef[:, 0])
    plt.axis((0, 255, 0, np.max(histRef)))

    plt.subplot(236, xticks=[], yticks=[])
    plt.title("4. Match result histogram")
    histDst = cv.calcHist([grayDst], [0], None, [256], [0, 255])
    plt.bar(range(256), histDst[:, 0])
    plt.axis((0, 255, 0, np.max(histDst)))

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    histogram_specification()