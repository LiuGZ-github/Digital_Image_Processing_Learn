import numpy as np
import cv2  as cv
from matplotlib import pyplot as plt
from pywin.Demos.cmdserver import flags


def images_mosaic():
    filepath = "../../statics/images/Lena.tif"
    img = cv.imread(filepath, flags=1)

    x, y, wroi, hroi = 208, 176, 155, 215
    imgROI = img[y:y+hroi, x:x+wroi].copy()

    plt.figure(figsize=(9, 6))
    plt.subplot(231),plt.title('1.Original'),plt.axis('off')
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

    plt.subplot(232),plt.title('2.ROI'),plt.axis('off')
    plt.imshow(cv.cvtColor(imgROI, cv.COLOR_BGR2RGB))

    mosaic = np.zeros(imgROI.shape, np.uint8)
    ksize = [5, 10, 20]
    for i in range(3):
        k = ksize[i]
        for h in range(0, hroi, k):
            for w in range(0, wroi, k):
                color = imgROI[h, w]
                mosaic[h:h + k, w:w + k, :] = color
        imgMosaic = img.copy()
        imgMosaic[y:y+hroi, x:x+wroi] = mosaic
        plt.subplot(2,3,i+4),plt.title("Coding image (size={})".format(k)),plt.axis('off')
        plt.imshow(cv.cvtColor(imgMosaic, cv.COLOR_BGR2RGB))

    plt.subplot(233),plt.title("3.Mosaic"),plt.axis('off')
    plt.imshow(cv.cvtColor(mosaic, cv.COLOR_BGR2RGB))
    plt.show()

if __name__ == '__main__':
    images_mosaic()