import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def select_ROI():
    img = cv.imread("../../statics/images/Lena.tif")

    # 鼠标框选矩形ROI
    rect = cv.selectROI("Select ROI", img, False)
    print(rect)

    # 裁剪获取选择的矩形ROI
    img2 = img[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
    cv.imshow("Select ROI", img2)
    cv.waitKey(0)
    cv.destroyAllWindows()

def onMouseAction(event, x, y, flags, param):
    global pts
    setpoint = (x, y)
    if event == cv.EVENT_LBUTTONDOWN:
        pts.append(setpoint)
        print(len(pts), setpoint, end='\n')
    elif event == cv.EVENT_MBUTTONDOWN:
        pts.pop()
    elif event == cv.EVENT_RBUTTONDOWN:
        param = False
        print("结束绘制，按 esc 键退出")

def mouse_interaction():
    img = cv.imread("../../statics/images/Lena.tif")
    imgCopy = img.copy()

    # 鼠标交互ROI
    cv.namedWindow('origin')
    cv.setMouseCallback('origin', onMouseAction)
    while True:
        if len(pts) > 0:
            cv.circle(imgCopy, pts[-1], 5, (0, 0, 255), -1)
        if len(pts) > 1:
            cv.line(imgCopy, pts[-1], pts[-2], (255, 0, 0), 2)
        cv.imshow('origin', imgCopy)
        key = cv.waitKey(10) & 0xFF
        if key == 27:
            break
    cv.destroyAllWindows()

    # 提取多边形
    print(pts)

    points = np.array(pts, np.int32)
    cv.polylines(img, [points], True, (255, 0, 0), 2)
    mask = np.zeros(img.shape[:2], np.uint8)
    cv.fillPoly(mask, [points], (255, 255, 255))
    imgROI = cv.bitwise_and(img, img, mask=mask)

    plt.figure(figsize=(9, 3.5))
    plt.subplot(131),plt.title("1. origin"), plt.axis('off')
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.subplot(132), plt.title("2. ROI"), plt.axis('off')
    plt.imshow(mask, cmap='gray')
    plt.subplot(133), plt.title("3. ROI crop"), plt.axis('off')
    plt.imshow(cv.cvtColor(imgROI, cv.COLOR_BGR2RGB))
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # select_ROI()
    pts = []
    mouse_interaction()