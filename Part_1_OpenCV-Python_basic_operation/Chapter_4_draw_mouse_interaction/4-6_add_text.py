import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def add_text():
    img1 = cv.imread("../../statics/images/Lena.tif")
    img2 = img1.copy()

    # (1)函数cv.putText()添加非中文文字
    text = "Digital Image Processing"
    fontList = [cv.FONT_HERSHEY_DUPLEX,
                cv.FONT_HERSHEY_SIMPLEX,
                cv.FONT_HERSHEY_COMPLEX,
                cv.FONT_HERSHEY_COMPLEX_SMALL,
                cv.FONT_ITALIC]
    fonScale = [0.2, 0.4, 0.6, 0.8, 1]
    fontColor = [(0, 0, 255), (0, 255, 0), (0, 255, 255), (128, 128, 128), (255, 255, 255)]
    for i in range(len(fontList)):
        pos = (10, 40 * (i + 1))
        cv.putText(img1, text, pos, fontList[i], fonScale[i], fontColor[i])

    cv.imshow("img1", img1)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    add_text()