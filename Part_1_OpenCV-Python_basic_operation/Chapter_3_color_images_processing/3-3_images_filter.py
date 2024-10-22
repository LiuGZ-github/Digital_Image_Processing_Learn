import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

def images_filter():
    img = cv.imread("../../statics/images/Fig0301.png", flags=1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]

    plt.figure(figsize=(9, 6))
    plt.subplot(231),plt.axis('off'), plt.title('Origin')
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

    cmList = ["cm.copper", "cm.hot", "cm.YIOrRd", "cm.rainbow", "cm.prism"]
    for i in range(len(cmList)):
        cmMap = eval(cmList[i])(np.arange(256))


if __name__ == '__main__':
    images_filter()
