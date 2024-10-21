import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def images_crop_joint():
    # (1) 图像的裁剪
    filepath = "../../statics/images/Lena.tif"
    img = cv.imread(filepath, flags=1)
    xmin, ymin, w, h = 180, 190, 200, 200
    imgCrop = img[ymin:ymin+h, xmin:xmin+w].copy()
    print("img:{}, imgCrop:{}".format(img.shape, imgCrop.shape))


    # (2) 图像的拼接
    logo = cv.imread("../../statics/images/Fig0201.png")
    imgH1 = cv.resize(img, (400, 400))
    imgH2 = cv.resize(logo, (300, 400))
    imgH3 = imgH2.copy()
    stackH = cv.hconcat((imgH1, imgH2, imgH3))
    plt.figure(figsize=(9, 4))
    plt.imshow(cv.cvtColor(stackH, cv.COLOR_BGR2RGB))
    plt.xlim(0, 1000), plt.ylim(400, 0)
    plt.show()

    imgV1 = cv.resize(img, (400, 400))
    imgV2 = cv.resize(logo, (400, 300))
    stackV = cv.vconcat((imgV1, imgV2))
    cv.imshow("StackV", stackV)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    images_crop_joint()