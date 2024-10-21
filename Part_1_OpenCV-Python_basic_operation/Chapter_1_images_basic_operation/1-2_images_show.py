import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def image_show():
    filepath = "../../statics/images/Lena.tif"
    img = cv.imread(filepath, flags=1)
    gray = cv.imread(filepath, flags=0)

    cv.imshow('Lena', img)  #显示图像
    cv.imshow("Lina_gray", gray)
    cv.waitKey(0)
    cv.destroyAllWindows()

def image_show2():
    filepath = "../../statics/images/Lena.tif"
    img = cv.imread(filepath, flags=1)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # 图片格式转换 BGR -> RGB
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # BGR -> Gray

    plt.figure(figsize=(8, 7))  # 创建自定义图像

    plt.subplot(221),plt.title("1. RGB (Matplotlib)"),plt.axis('off')
    plt.imshow(imgRGB)

    plt.subplot(222),plt.title("2. BGR (OpenCV)"),plt.axis('off')
    plt.imshow(img)

    plt.subplot(223),plt.title("3. cmap='gray'"),plt.axis('off')  # 用Matplotlib显示灰度图像，设置gray参数
    plt.imshow(gray, cmap='gray')

    plt.subplot(224),plt.title("4. without cmap"),plt.axis('off')  # 用Matplotlib显示灰度图像，未设置gray参数
    plt.imshow(gray)

    plt.tight_layout()  # 自动调整子图间隔
    plt.show()

if __name__ == '__main__':
    image_show()
    # image_show2()