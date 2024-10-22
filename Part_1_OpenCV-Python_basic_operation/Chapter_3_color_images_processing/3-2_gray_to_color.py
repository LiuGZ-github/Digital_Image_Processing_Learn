import cv2 as cv
import numpy as np
from PIL.ImageChops import composite
from fontTools.mtiLib import parseMarkToLigature
from matplotlib import pyplot as plt

def gray_to_color():
    gray = cv.imread("../../statics/images/Fig0301.png", flags=0)
    h, w = gray.shape[:2]

    # 伪彩色处理
    img1 = cv.applyColorMap(gray, colormap=cv.COLORMAP_HOT)
    img2 = cv.applyColorMap(gray, colormap=cv.COLORMAP_PINK)
    img3 = cv.applyColorMap(gray, colormap=cv.COLORMAP_RAINBOW)
    img4 = cv.applyColorMap(gray, colormap=cv.COLORMAP_HSV)
    img5 = cv.applyColorMap(gray, colormap=cv.COLORMAP_TURBO)

    plt.figure(figsize=(9, 6))
    images = [gray, img1, img2, img3, img4, img5]
    titles = ['GRAY', 'HOT', 'PINK', 'RAINBOW', 'HSV', 'Turbo']
    for i in range(len(images)):
        plt.subplot(2, 3, i + 1),plt.title(titles[i]),plt.axis('off')
        plt.imshow(images[i])
    plt.tight_layout()
    plt.show()

def gray_to_color2():
    # 读取蟹状星云 (Crab Nebula) 光谱图
    composite = cv.imread("../../statics/images/Fig0303.png", flags=1)  # 读取 NASA 合成图像
    grayOpti = cv.imread("../../statics/images/Fig0303a.jpg", flags=0)  # 读取 Optical
    grayXray = cv.imread("../../statics/images/Fig0303b.jpg", flags=0)  # 读取 Xray
    grayInfr = cv.imread("../../statics/images/Fig0303c.jpg", flags=0)  # 读取 Infrared
    h, w = grayOpti.shape[:2]  # 图片的高度, 宽度

    # # 伪彩色处理
    # pseudoXray = cv.applyColorMap(grayXray, colormap=cv.COLORMAP_TURBO)
    # pseudoOpti = cv.applyColorMap(grayOpti, colormap=cv.COLORMAP_MAGMA)
    # pseudoInfr = cv.applyColorMap(grayInfr, colormap=cv.COLORMAP_HOT)

    # 多光谱编码合成
    compose1 = np.zeros((h, w, 3), np.uint8)  # 创建黑色图像 BGR=0
    compose1[:, :, 0] = grayOpti  # Optical -> B
    compose1[:, :, 1] = grayXray  # Xray -> G
    compose1[:, :, 2] = grayInfr  # Infrared -> R
    compose2 = np.zeros((h, w, 3), np.uint8)  # 创建黑色图像 BGR=0
    compose2[:, :, 0] = grayXray  # Xray -> B
    compose2[:, :, 1] = grayOpti  # Optical -> G
    compose2[:, :, 2] = grayInfr  # Infrared -> R

    plt.figure(figsize=(9, 6))
    plt.subplot(231), plt.axis('off'), plt.title("(1) CrabNebula-Xray")
    plt.imshow(grayXray, cmap='gray')
    plt.subplot(232), plt.axis('off'), plt.title("(2) CrabNebula-Optical")
    plt.imshow(grayOpti, cmap='gray')
    plt.subplot(233), plt.axis('off'), plt.title("(3) CrabNebula-Infrared")
    plt.imshow(grayInfr, cmap='gray')
    plt.subplot(234), plt.axis('off'), plt.title("(4) Composite pseudo 1")
    plt.imshow(cv.cvtColor(compose1, cv.COLOR_BGR2RGB))
    plt.subplot(235), plt.axis('off'), plt.title("(5) Composite pseudo 2")
    plt.imshow(cv.cvtColor(compose2, cv.COLOR_BGR2RGB))
    plt.subplot(236), plt.axis('off'), plt.title("(6) Composite by NASA")
    plt.imshow(cv.cvtColor(composite, cv.COLOR_BGR2RGB))
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # gray_to_color()
    gray_to_color2()