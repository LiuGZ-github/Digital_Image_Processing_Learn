import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def images_bitwise():
    img = cv.imread("../../statics/images/Lena.tif", flags=0)

    # 加载或生成水印信息
    binary = np.zeros(img.shape[:2], np.uint8)
    cv.putText(binary, str(np.datetime64('today')), (50, 200), cv.FONT_HERSHEY_SIMPLEX, 2, (1, 0, 0), 2)
    cv.putText(binary, str(np.datetime64('now')), (50, 250), cv.FONT_HERSHEY_DUPLEX, 1, (1, 0, 0))
    cv.putText(binary, "Copyright: youcans@qq.com", (50, 300), cv.FONT_HERSHEY_DUPLEX, 1, (1, 0, 0))


    # 向原始图像嵌入水印
    imgH7 = cv.bitwise_and(img, 254)  # 按位与运算，图像最低位 LSB=0
    imgMark = cv.bitwise_or(imgH7, binary)  # (p7,p6,...pg7,g6,...1,b)

    # 从嵌入水印图像中提取水印
    extract = cv.bitwise_and(imgMark, 1)  # 按位与运算，取图像的最低位 LSB

    plt.figure(figsize=(9, 3.5))
    plt.subplot(131), plt.title("1. Original"), plt.axis('off')
    plt.imshow(img, cmap='gray')
    plt.subplot(132), plt.title("2. Embedded watermark"), plt.axis('off')
    plt.imshow(imgMark, cmap='gray')
    plt.subplot(133), plt.title("3. Extracted watermark"), plt.axis('off')
    plt.imshow(extract, cmap='gray')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    images_bitwise()

