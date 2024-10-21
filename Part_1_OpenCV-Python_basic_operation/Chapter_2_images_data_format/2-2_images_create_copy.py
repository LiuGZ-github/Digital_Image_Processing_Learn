import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os


def images_create_copy():

    # 通过宽度、高度值创建RGB彩色图像
    height, width, ch = 400, 300, 3
    imgEmpty = np .empty((height, width, ch), dtype=np.uint8)  # 创建空白数组
    imgBlack = np .zeros((height, width, ch), dtype=np.uint8)  # 创建黑色图像
    imgWhite = np.ones((height, width, ch), dtype=np.uint8) * 255  # 创建白色图像

    plt.figure(figsize=(10, 8))
    plt.subplot(1,2,1),plt.title("black image"),plt.axis('off')
    plt.imshow(imgBlack)

    plt.subplot(1,2,2),plt.title("white image"),plt.axis('on')
    plt.imshow(imgWhite)
    plt.show()


    # 创建与已有图像形状相同的新图像
    img = cv.imread("../../statics/images/Lena.tif", flags=1)
    imgBlackLike = np.zeros_like(img)
    imgWhiteLike = np.ones_like(img) * 255
    plt.figure(figsize=(10, 8))
    plt.subplot(1,2,1),plt.title("black image like"),plt.axis('off')
    plt.imshow(imgBlackLike)
    plt.subplot(1,2,2),plt.title("white image like"),plt.axis('on')
    plt.imshow(imgWhiteLike)
    plt.show()

    # 创建彩色随机图像
    randomByteArray = bytearray(os.urandom(height * width * ch))  # 产生随机数组
    flatArray = np.array(randomByteArray)  # 转换为Numpy一维数组
    imgRGBRand1 = flatArray.reshape(height, width, ch)
    imgRGBRand2 = flatArray.reshape(width, height, ch)
    plt.figure(figsize=(10, 8))
    plt.subplot(1,2,1),plt.title("random byte array"),plt.axis('off')
    plt.imshow(imgRGBRand1)
    plt.subplot(1,2,2),plt.title("random byte array"),plt.axis('off')
    plt.imshow(imgRGBRand2)
    plt.tight_layout()
    plt.show()

    # 创建灰度图像
    grayWhite = np.ones((height, width), dtype=np.uint8) * 255
    grayBlack = np.zeros((height, width), dtype=np.uint8)
    grayEye = np.eye(width)
    randomByteArray = bytearray(os.urandom(height * width))
    flatArray = np.array(randomByteArray)
    imgGrayRand = flatArray.reshape(height, width)

    plt.figure(figsize=(10, 8))

    plt.subplot(2,2,1),plt.title("gray white image"),plt.axis('on')
    plt.imshow(grayWhite, cmap='gray',vmin=0, vmax=255)

    plt.subplot(2,2,2),plt.title("gray black image"),plt.axis('off')
    plt.imshow(grayBlack, cmap='gray',vmin=0, vmax=255)

    plt.subplot(2,2,3),plt.title("gray eye"),plt.axis('off')
    plt.imshow(grayEye, cmap='gray',vmin=0, vmax=255)

    plt.subplot(2,2,4),plt.title("random byte array"),plt.axis('off')
    plt.imshow(imgGrayRand, cmap='gray',vmin=0, vmax=255)

    plt.tight_layout()
    plt.show()

    # 图像的复制
    img1 = img.copy()  # 深拷贝
    img1[:,:,:] = 0
    cv.imshow('img', img)
    cv.imshow('img1', img1)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    images_create_copy()