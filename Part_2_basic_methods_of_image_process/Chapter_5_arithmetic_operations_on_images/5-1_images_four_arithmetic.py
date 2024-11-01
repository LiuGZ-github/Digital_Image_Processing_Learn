import numpy as np
import cv2 as cv

def images_add():
    img1 = cv.imread("../../statics/images/Lena.tif")

    img2 = cv.imread("../../statics/images/Fig0301.png")
    h, w = img1.shape[:2]
    img3 = cv.resize(img2, (w, h))
    gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    print(img1.shape, img2.shape, img3.shape, gray.shape)

    # (1) 图像与常数相加
    value = 100
    imgAddV = cv.add(img1, np.ones_like(img1) * value)
    imgAddG = cv.add(gray, np.ones_like(gray) * value)
    cv.imshow("imgAddV", imgAddV)
    cv.imshow("imgAddG", imgAddG)

    # (2) 图像与标量相加
    scalar = (100, 0, 0, 0)
    imgAddS = cv.add(img1, np.array(scalar))
    imgAddGS = cv.add(gray, np.array(scalar))
    cv.imshow("imgAddS", imgAddS)
    cv.imshow("imgAddGS", imgAddGS)

    cv.waitKey(0)
    cv.destroyAllWindows()


def mask_images_process():
    img1 = cv.imread("../../statics/images/Lena.tif")
    img2 = cv.imread("../../statics/images/Fig0301.png")
    h, w = img1.shape[:2]
    img3 = cv.resize(img2, (w, h))
    imgAddV = cv.add(img1, img3)

    # 掩膜加法, 矩形掩膜图像
    maskRec = np.zeros(img1.shape[:2], np.uint8)
    xmin, ymin, w, h = 170, 190, 200, 200
    maskRec[ymin:ymin+h, xmin:xmin+w] = 255
    imgAddRec = cv.add(img1, img3, mask=maskRec)

    # 掩膜加法，圆心掩膜加法
    maskCir = np.zeros(img1.shape[:2], np.uint8)
    cv.circle(maskCir, (280, 280), 120, (255, 0, 0), -1)
    imgAddCir = cv.add(img1, img3, mask=maskCir)

    cv.imshow("imgAddV", imgAddV)
    cv.imshow("imgAddRec", imgAddRec)
    cv.imshow("imgAddCir", imgAddCir)
    cv.waitKey(0)
    cv.destroyAllWindows()

def images_weight_add():
    img1 = cv.imread("../../statics/images/Lena.tif")
    img2 = cv.imread("../../statics/images/Fig0301.png")
    h, w = img1.shape[:2]
    img3 = cv.resize(img2, (w, h))
    imgAddCV = cv.add(img1, img3)

    # 两幅图像的加权加法
    a, b = 0.25, 0.75
    imgAddW1 = cv.addWeighted(img1, a, img3, b, 0)
    a, b = 0.5, 0.5
    imgAddW2 = cv.addWeighted(img1, a, img3, b, 0)
    a, b = 0.75, 0.25
    imgAddW3 = cv.addWeighted(img1, a, img3, b, 0)

    # 两幅图像实现渐变
    wList = np.arange(0.0, 1.0, 0.03
                      )
    for i in wList:
        imgW = cv.addWeighted(img1, i, img3, 1- i, 0)
        cv.imshow("imgW", imgW)
        cv.waitKey(150)

    # cv.imshow("imgAddCV", imgAddCV)
    # cv.imshow("imgAddW1", imgAddW1)
    # cv.imshow("imgAddW2", imgAddW2)
    # cv.imshow("imgAddW3", imgAddW3)
    # cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    images_add()
    # mask_images_process()
    # images_weight_add()
