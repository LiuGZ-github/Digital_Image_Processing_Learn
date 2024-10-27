import cv2 as cv
from matplotlib import pyplot as plt

def gif_images_read_save():
    # 读取单幅图像，支持BMP、JPG、PNG、TIFF等常用格式
    img1 = cv.imread("../../statics/images/FVid1.png")
    img2 = cv.imread("../../statics/images/FVid2.png")
    img3 = cv.imread("../../statics/images/FVid3.png")
    img4 = cv.imread("../../statics/images/FVid4.png")
    imgList = [img1, img2, img3, img4]

    # 保存多帧图像
    saveFile = "../../statics/images/gif_images/imgList.tiff"
    ret = cv.imwritemulti(saveFile, imgList)
    if ret:
        print("Image List Write Successes in {}".format(saveFile))
        print("len(imgList):", len(imgList))

    # 读取多帧图像
    imgMulti = cv.imreadmulti(saveFile)
    print("len(imgList):", len(imgList))

    for i in range(len(imgList)):
        cv.imshow("imgList", imgList[i])
        cv.waitKey(1000)
    cv.destroyAllWindows()

if __name__ == "__main__":
    gif_images_read_save()