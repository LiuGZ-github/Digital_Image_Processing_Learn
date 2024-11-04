import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def color_image_histogram_specification():
    imgSrc = cv.imread("../../statics/images/Fig0801.png", flags=1)
    imgRef = cv.imread("../../statics/images/Fig0301.png", flags=1)

    imgDst = np.ones_like(imgSrc)
    for i in range(imgSrc.shape[2]):
        # 计算累计直方图
        histSrc = cv.calcHist([imgSrc], [i], None, [256], [0, 256])
        histRef = cv.calcHist([imgRef], [i], None, [256], [0, 256])
        cdfSrc = np.cumsum(histSrc)
        cdfRef = np.cumsum(histRef)
        cdfSrc = cdfSrc / cdfSrc[-1]
        cdfRef = cdfRef / cdfRef[-1]
        for j in range(256):
            tmp = abs(cdfSrc[j] - cdfRef)
            tmp = tmp.tolist()
            index = tmp.index(min(tmp))
            imgDst[:, :, i][imgSrc[:, :, i]  == j]  = index

if __name__ == '__main__':
    color_image_histogram_specification()