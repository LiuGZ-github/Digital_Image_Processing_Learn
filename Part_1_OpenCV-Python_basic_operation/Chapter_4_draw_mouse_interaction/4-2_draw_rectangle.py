import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def draw_rectangle():
    height, width, channels = 300, 320, 3
    img = np.ones((height, width, channels), dtype='uint8') * 192

    img1 = img.copy()
    cv.rectangle(img1, (0, 80), (100, 220), (0, 0, 255), 2)
    cv.rectangle(img1, (80, 0), (220, 100), (0, 255, 0), 2)
    cv.rectangle(img1, (150, 120), (400, 200), (255, 0, 0), 2)
    cv.rectangle(img1, (50, 250), (100, 290), (128, 0, 0), -1)  # 内部填充

    img2 = img.copy()
    x, y, w, h = (50, 100, 200, 100)
    cv.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv.imshow('rectangle1', img1)
    cv.imshow('rectangle2', img2)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    draw_rectangle()
