import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def draw_polyline():
    img = np.ones((900, 400, 3), np.uint8) * 200
    img1 = img.copy()
    img2 = img.copy()
    img3 = img.copy()
    img4 = img.copy()

    # 多边形顶点
    points1 = np.array([[200, 60], [295, 129], [259, 241], [141, 241], [105, 129]], np.int32)
    points2 = np.array([[200, 350], [259, 531], [105, 419], [295, 419], [141, 531]], np.int32)
    points3 = np.array([[200, 640], [222, 709], [295, 709], [236, 752], [259, 821],
                               [200, 778], [141, 821], [164, 752], [105, 709], [178, 709]], np.int32)
    print(points1.shape, points2.shape, points3.shape)

    # 绘制多边形，闭合曲线
    pts1 = [points1]
    cv.polylines(img1, pts1, True, (0, 0, 255))
    cv.polylines(img1, [points2, points3], True, (0, 0, 255))

    # 绘制多边形，曲线不闭合
    cv.polylines(img2, [points1], False, (0, 0, 255))
    cv.polylines(img2, [points2, points3], False, (0, 0, 255))

    # 绘制填充多边形，注意交叉重叠部分
    cv.fillPoly(img3, [points1], (0, 0, 255))
    cv.fillPoly(img3, [points2, points3], (0, 0, 255))

    cv.fillConvexPoly(img4, points1, (0, 0, 255))
    cv.fillConvexPoly(img4, points2, (0, 0, 255))  # 不能绘制存在自相交的多边形
    cv.fillConvexPoly(img4, points3, (0, 0, 255))  # 可以绘制凹多边形，弹药慎用

    # cv.imshow('img1', img1)
    # cv.imshow('img2', img2)
    # cv.imshow('img3', img3)
    cv.imshow('img4', img4)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    draw_polyline()

