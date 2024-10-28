import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def draw_rotate_rect():
    height, width , channels = 300, 400, 3
    img = np.ones((height, width, channels), np.uint8) * 192

    # (1) 围绕矩形中心旋转
    cx, cy, w, h = (200, 150, 200, 100)  # 定义矩形的中心坐标、长和宽
    img1 = img.copy()
    cv.circle(img1, (cx, cy), 4, (0, 0, 255), thickness=-1)  # 旋转中心
    angle = [0, 15, 30, 45, 60, 75, 90]
    box = np.zeros((4, 2), np.int32)  # 存储旋转后四个顶点的坐标
    for i in range(len(angle)):
        rect = ((cx, cy), (w, h), angle[i])
        box = np.int32(cv.boxPoints(rect))
        color = (30 * i, 0, 255 - 30 * i)
        cv.drawContours(img1, [box], 0, color, 1)

    # (2) 围绕矩形左上顶点旋转
    x, y, w, h = (200, 100, 160, 100)
    img2 = img.copy()
    cv.circle(img2, (x, y), 4, (0, 0, 255), thickness=-1)
    angle = [0, 15, 30, 45, 60, 75, 90]
    for i in range(len(angle)):
        ang = angle[i] * np.pi / 180  # 角度转弧度
        x1, y1 = x, y
        x2 = int(x + w * np.cos(ang))
        y2 = int(y + w * np.sin(ang))
        x3 = int(x + w * np.cos(ang) - h * np.sin(ang))
        y3 = int(y + w * np.sin(ang) + h * np.cos(ang))
        x4 = int(x - h * np.sin(ang))
        y4 = int(y + h * np.cos(ang))
        box = np.array([[x1, y1], [x2,  y2], [x3, y3], [x4, y4]])
        color = (30 * i, 0, 255 - 30 * i)
        cv.drawContours(img2, [box], 0, color, 1)

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    draw_rotate_rect()