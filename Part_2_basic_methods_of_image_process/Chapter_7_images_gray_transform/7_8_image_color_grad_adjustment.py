import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def levelsAdjust(img, Sin=0, Hin=255, Mt=1.0, Sout=0, Hout=255):
    Sin = min(max(Sin, 0), Hin - 2)
    Hin = min(Hin, 255)
    Mt = min(max(Mt, 0.01), 9.99)
    Sout = min(max(Sout, 0), Hout - 2)
    Hout = min(Hout, 255)
    difin = Hin - Sin
    difout = Hout - Sout
    table = np.zeros(difin, np.uint16)
    for i in range(256):
        V1 = min(max(255 * (i - Sin) / difin, 0), 255)
        V2 = 255 * np.power( (V1 / 255), (1 / Mt))
        table[i] = min(max(Sout + difout * V2/ 255, 0), 255)
    imgTone = cv.LUT(img, table)
    return imgTone

if __name__ == '__main__':
    gray = cv.imread("../../statics/images", 0)


