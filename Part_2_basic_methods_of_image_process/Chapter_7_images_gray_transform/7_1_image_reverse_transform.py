import cv2 as cv
import numpy as np

def image_reverse_transform():
    filepath = "../../statics/images/Lena.tif"
    img= cv.imread(filepath, flags=1)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    # LUT 快速查表
    transTable = np.array([(255 - i) for i in range(256)]).astype("uint8")
    imgInv = cv.LUT(img, transTable)
    grayInv = cv.LUT(gray, transTable)
    cv.imshow("Image", img)
    cv.imshow("Gray", gray)
    cv.imshow("Inverse", imgInv)
    cv.imshow("gray2", grayInv)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    image_reverse_transform()