import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def draw_line():
    height, width, channels = 180, 200, 3
    img = np.ones((height, width, channels), dtype='uint8') * 160

    # (1) 线条参数color的设置
    img1 = img.copy()
    cv.line(img1, (0,0), (200, 180), (0, 0, 255), 1)
    cv.line(img1, (0,0), (100, 180), (0, 255, 0), 1)
    cv.line(img1, (0,40), (200, 40), (128, 0, 0), 2)
    cv.line(img1, (0, 80), (200, 80), (128, 0, 0), 2)
    cv.line(img1, (0, 120), (200, 100), (255, 0, 0), 2)

    # (2) 线宽的设置
    img2 = img.copy()
    cv.line(img2, (20,500), (180, 10), (255, 0, 0), 1, cv.LINE_8)
    cv.line(img2, (20, 90), (180, 50), (255, 0, 0), 1, cv.LINE_AA)

    # tipLength 指箭头部分长度与整个线段长度的比例
    img3 = img.copy()
    img3 = cv.arrowedLine(img, (20, 20), (180, 20), (0, 0, 255), tipLength=0.1)


    cv.imshow('img', img)
    cv.imshow("img1", img1)
    cv.imshow("img2", img2)
    cv.imshow("img3", img3)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    draw_line()