import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import yticks


def histogram_equalization():
    gray = cv.imread("../../statics/images/Fig0702.png", flags=0)
    histSrc = cv.calcHist([gray], [0], None, [256], [0, 256])

    # 直方图均衡化
    grayEqualize = cv.equalizeHist(gray)
    histEqual = cv.calcHist([grayEqualize], [0], None, [256], [0, 256])

    # 直方图归一化
    grayNorm = cv.normalize(gray, None, 0., 255., cv.NORM_MINMAX)
    histNorm = cv.calcHist([grayNorm], [0], None, [256], [0, 256])

    plt.figure(figsize=(9, 6))

    plt.subplot(231), plt.axis("off"), plt.title('1. original')
    plt.imshow(gray, cmap='gray', vmin=0, vmax=255)

    plt.subplot(232), plt.axis("off"), plt.title('2. normalized')
    plt.imshow(grayNorm, cmap='gray', vmin=0, vmax=255)

    plt.subplot(233), plt.axis('off'), plt.title('3. hist-equalized')
    plt.imshow(grayEqualize, cmap='gray', vmin=0, vmax=255)

    plt.subplot(234, yticks=[]), plt.axis((0., 255., 0., float(np.max(histSrc))))
    plt.title("4. gray hist of src")
    plt.bar(range(256), histSrc[:, 0])

    plt.subplot(235, yticks=[]), plt.axis((0., 255., 0., float(np.max(histEqual))))
    plt.title("5. histogram equalization")
    plt.bar(range(256), histNorm[:, 0])

    plt.subplot(236, yticks=[]), plt.axis((0., 255., 0., float(np.max(histNorm))))
    plt.title("6. histogram equalization")
    plt.bar(range(256), histNorm[:, 0])

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    histogram_equalization()
