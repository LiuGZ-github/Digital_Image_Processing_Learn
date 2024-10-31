import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def integral_image():
    img = cv.imread("../../statics/images/Lena.tif", flags=0)
    H, W = img.shape[:2]

    k = 15  # 均值滤波器的尺寸
    # (1) 两重循环卷积运算实现均值滤波
    timeBegin = cv.getTickCount()
    pad = k // 2 + 1
    imgPad = cv.copyMakeBorder(img, pad, pad, pad, pad, cv.BORDER_REFLECT)
    imgBox1 = np.zeros((H, W), np.int32)
    for h in range(H):
        for w in range(W):
            imgBox1[h, w] = np.sum(imgPad[h:h+k, w:w+k]) / (k * k)
    timeEnd = cv.getTickCount()
    print((timeEnd - timeBegin) / cv.getTickFrequency())

    # (2) 基于积分图像方法实现均值滤波
    timeBegin = cv.getTickCount()
    pad = k // 2 + 1
    imgPad2 = cv.copyMakeBorder(img, pad, pad, pad, pad, cv.BORDER_REFLECT)
    sumImg = cv.integral(imgPad2)
    imgBox2 = np.zeros((H, W), np.uint8)
    imgBox2[:, :] = (sumImg[k:k + H, k:k + W] - sumImg[0:H, k:W + k] - sumImg[k: k + H, 0: W] + sumImg[0: H, 0: W]) / (k * k)
    timeEnd = cv.getTickCount()
    print((timeEnd - timeBegin) / cv.getTickFrequency())

    # (3) 函数cv.boxFilter实现均值滤波
    timeBegin = cv.getTickCount()
    kernel = np.ones(k, np.float32) / (k * k)
    imgBoxF = cv.boxFilter(img, -1, (k, k))
    timeEnd = cv.getTickCount()
    print((timeEnd - timeBegin) / cv.getTickFrequency())

    plt.figure(figsize=(9, 6))
    plt.subplot(131), plt.axis('off'), plt.title("original image")
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.subplot(132), plt.axis('off'), plt.title("2")
    plt.imshow(imgBox1, cmap='gray', vmin=0, vmax=255)
    plt.subplot(133), plt.axis('off'), plt.title("3")
    plt.imshow(imgBox2, cmap='gray', vmin=0, vmax=255)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    integral_image()