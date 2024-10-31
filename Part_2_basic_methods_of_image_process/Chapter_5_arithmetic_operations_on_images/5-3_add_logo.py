import cv2 as cv

def add_logo():
    img = cv.imread("../../statics/images/Lena.tif")
    logo = cv.imread("../../statics/images/logoCV.png")
    h2, w2 = logo.shape[:2]
    imgROI = img[:h2, :w2]

    # (1) 灰度化、二值化，生成掩膜图像
    gray = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
    _, mask = cv.threshold(gray, 175, 255, cv.THRESH_BINARY_INV)

    # (2) 带掩膜的位操作，生成图像的背景和前景
    background = cv.bitwise_and(imgROI, imgROI, mask=cv.bitwise_not(mask))  # 生成合成背景
    foreground = cv.bitwise_and(logo, logo, mask=mask)
    compositeROI = cv.add(background, foreground)
    composite = img.copy()
    composite[:h2, :w2] = compositeROI

    # (3) 直接替换
    composite2 = img.copy()
    composite2[:h2, :w2] = logo
    cv.imshow('composite2', composite2)

    # (4)直接相加
    composite3 = img.copy()
    composite3[:h2, :w2] = cv.add(composite3[:h2, :w2], logo)
    cv.imshow('composite3', composite3)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    add_logo()