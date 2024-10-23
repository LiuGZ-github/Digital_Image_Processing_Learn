import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def images_color_adjust():
    img = cv.imread("../../statics/images/Lena.tif", flags=1)

    # 生成单通道LUT，形状为(256,)
    maxG = 128  # 修改颜色通道最大值，0 <= maxG <= 255
    lutHalf = np.array([int(i * maxG / 255) for i in range(256)]).astype("uint8")
    lutEqual = np.array([i for i in range(256)]).astype("uint8")
    # 构造多通道LUT,形状为(1, 256, 3)
    lut3halfB = np.dstack((lutHalf, lutEqual, lutEqual))
    print(lut3halfB)
    lut3halfG = np.dstack((lutEqual, lutHalf, lutEqual))
    lut3halfR = np.dstack((lutEqual, lutEqual, lutHalf))
    # 用多通道LUT进行颜色替换
    blendHalfB = cv.LUT(img, lut3halfB)
    blendHalfG = cv.LUT(img, lut3halfG)
    blendHalfR = cv.LUT(img, lut3halfR)

    plt.figure(figsize=(9, 3.5))
    plt.subplot(131),plt.axis('off'),plt.title('1. B_ch half')
    plt.imshow(cv.cvtColor(blendHalfB, cv.COLOR_BGR2RGB))
    plt.subplot(132),plt.axis('off'),plt.title('2. G_ch half')
    plt.imshow(cv.cvtColor(blendHalfG, cv.COLOR_BGR2RGB))
    plt.subplot(133),plt.axis('off'),plt.title('3. R_ch half')
    plt.imshow(cv.cvtColor(blendHalfR, cv.COLOR_BGR2RGB))
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    images_color_adjust()