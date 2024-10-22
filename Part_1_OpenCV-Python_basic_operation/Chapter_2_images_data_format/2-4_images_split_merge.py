import matplotlib.pyplot as plt
from fontTools.misc.psOperators import ps_boolean
import numpy as np
import cv2 as cv

def images_split_merge():
     filepath = "../../statics/images/Lena.tif"
     img = cv.imread(filepath, flags=1)

     # (1) cv.split 实现图像通道的拆分
     bImg, gImg, rImg = cv.split(img)
     print(bImg)

     # (2) cv.merge 实现图像通道的合并
     imgMerge = cv.merge((bImg, gImg, rImg))
     print(imgMerge)

     # (3) Numpy 拼接实现图像通道的合并
     imgStack = np.stack((bImg, gImg, rImg), axis=2)
     print(imgStack)

     # cv.imshow("bImg", bImg)
     # cv.imshow("gImg", gImg)
     # cv.imshow("rImg", rImg)
     # cv.imshow("imgMerge", imgMerge)
     # cv.waitKey(0)
     # cv.destroyAllWindows()

     # (3) Numpy切片提取颜色分量

     # 提取 B 通道
     imgB = img.copy()
     imgB[:, :, 1] = 0
     imgB[:, :, 2] = 0

     imgG = img.copy()
     imgG[:, :, 0] = 0
     imgG[:, :, 2] = 0

     imgR = img.copy()
     imgR[:, :, 0] = 0
     imgR[:, :, 1] = 0

     imgGR = img.copy()
     imgGR[:, :, 0] = 0

     plt.figure(figsize=(8, 7))
     plt.subplot(221),plt.title('1. B'),plt.axis('off')
     plt.imshow(cv.cvtColor(imgB, cv.COLOR_BGR2RGB))

     plt.subplot(222),plt.title('2. G'),plt.axis('off')
     plt.imshow(cv.cvtColor(imgG, cv.COLOR_BGR2RGB))

     plt.subplot(223),plt.title('3. R'),plt.axis('off')
     plt.imshow(cv.cvtColor(imgR, cv.COLOR_BGR2RGB))

     plt.subplot(224),plt.title('4. GR'),plt.axis('off')
     plt.imshow(cv.cvtColor(imgGR, cv.COLOR_BGR2RGB))

     plt.tight_layout()
     # plt.show()

if __name__ == '__main__':
     images_split_merge()