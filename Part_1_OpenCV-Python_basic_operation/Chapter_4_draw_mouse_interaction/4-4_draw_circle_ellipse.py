import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def draw_circle():
    img = np.ones((400, 600, 3), np.uint8) * 128

    center = (0, 0)
    cx, cy = 300, 200
    for r in range(200, 0, -20):
        color = (r, r, 255 - r)
        cv.circle(img,(cx, cy), r, color, -1)
        cv.circle(img, center, r, (255, 0, 0))
        cv.circle(img, (600, 400), r, color, 5)

    plt.figure(figsize=(10, 10))
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()

def draw_ellipse():
    pass

if __name__ == '__main__':
    draw_circle()