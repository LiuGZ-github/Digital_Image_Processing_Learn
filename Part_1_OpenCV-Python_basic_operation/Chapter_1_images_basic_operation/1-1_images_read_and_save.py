import cv2 as cv
import numpy as np
import urllib.request as request

def images_read_and_save():
    # 读取图像文件，支持BMP、JPG、PNG、TIFF
    filepath ="../../statics/images/p1.png"
    img = cv.imread(filepath, flags=1)  # flags=1 读取彩色图像
    gray = cv.imread(filepath, flags=0) # flags=0 读取灰色图像

    # 保存图像
    saveFile="../../statics/images/p1.jpg"
    cv.imwrite(saveFile, img, [int(cv.IMWRITE_JPEG_QUALITY), 8])
    cv.imwrite("../../statics/images/p2.jpg", gray)

    # 从网络读取图像
    response = request.urlopen("https://app7169.acapp.acwing.com.cn//static/image/menu/background.jpg")
    imgUrl = cv.imdecode(np.array(bytearray(response.read()), dtype=np.uint8), -1)
    cv.imshow("imgUrl", imgUrl)  # 在窗口显示图像
    key = cv.waitKey(3000)  # 3000毫秒后自动关闭
    cv.destroyAllWindows()


if __name__=="__main__":
    images_read_and_save()