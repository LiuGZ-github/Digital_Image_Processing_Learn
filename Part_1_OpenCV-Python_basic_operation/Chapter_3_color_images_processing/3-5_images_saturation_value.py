import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def images_saturation_value():
    img = cv.imread("../../statics/images/Lena.tif", flags=1)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    k = 0.5
    lutWeaken = np.array([int(k * i) for i in range(256)]).astype(np.uint8)
    lutEqual = np.array([i for i in range(256)]).astype(np.uint8)
    lutRaise = np.array([int(255 * (1 - k) + k * i) for i in range(256)]).astype(np.uint8)

    lutSWeaken = np.dstack((lutEqual, lutWeaken, lutEqual))
    lutSRaise = np.dstack((lutEqual, lutEqual, lutEqual))

    lutVWeaken = np.dstack((lutEqual, lutEqual, lutWeaken))
    lutVRaise = np.dstack((lutEqual, lutEqual, lutRaise))

    blendSWeaken = cv.LUT(hsv, lutSWeaken)
    blendSRaise = cv.LUT(hsv, lutSRaise)
    blendVWeaken = cv.LUT(hsv, lutVWeaken)
    blendVRaise = cv.LUT(hsv, lutVRaise)

    plt.figure(figsize=(9, 6))
    plt.subplot(231),plt.axis('off'), plt.title('1. s weaken')
    plt.imshow(cv.cvtColor(blendSWeaken, cv.COLOR_HSV2RGB))
    plt.subplot(232),plt.axis('off'), plt.title('2. original s')
    plt.imshow(cv.cvtColor(hsv, cv.COLOR_HSV2RGB))
    plt.subplot(233),plt.axis('off'), plt.title('3. s raise')
    plt.imshow(cv.cvtColor(blendSRaise, cv.COLOR_HSV2RGB))
    plt.subplot(234),plt.axis('off'), plt.title('4. v weaken')
    plt.imshow(cv.cvtColor(blendVWeaken, cv.COLOR_HSV2RGB))
    plt.subplot(235),plt.axis('off'), plt.title('5. original v')
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.subplot(236),plt.axis('off'), plt.title('6. v raise')
    plt.imshow(cv.cvtColor(blendVRaise, cv.COLOR_HSV2RGB))
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    images_saturation_value()