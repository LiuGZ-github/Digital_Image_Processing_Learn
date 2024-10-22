import cv2 as cv
from matplotlib import pyplot as plt


def images_color_space_conversion():
    imgBGR = cv.imread("../../statics/images/Lena.tif", flags=1)

    imgRGB = cv.cvtColor(imgBGR, cv.COLOR_BGR2RGB)
    imgGRAY = cv.cvtColor(imgBGR, cv.COLOR_BGR2GRAY)
    imgHSV = cv.cvtColor(imgBGR, cv.COLOR_BGR2HSV)
    imgYCrCb = cv.cvtColor(imgBGR, cv.COLOR_BGR2YCrCb)
    imgHLS = cv.cvtColor(imgBGR, cv.COLOR_BGR2HLS)
    imgXYZ = cv.cvtColor(imgBGR, cv.COLOR_BGR2XYZ)
    imgLAB = cv.cvtColor(imgBGR, cv.COLOR_BGR2LAB)
    imgYUV = cv.cvtColor(imgBGR, cv.COLOR_BGR2YUV)

    titles = ['BGR', 'RGB', 'GRAY', 'HSV', 'YCrCb', 'HLS', 'XYZ', 'LAB', 'YUV']
    images = [imgBGR, imgRGB, imgGRAY, imgHSV, imgYCrCb, imgHLS, imgXYZ, imgLAB, imgYUV]
    plt.figure(figsize=(10, 8))
    for i in range(len(images)):
        plt.subplot(3, 3, i + 1),plt.title(titles[i]),plt.axis('off')
        plt.imshow(images[i], cmap='gray')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    images_color_space_conversion()