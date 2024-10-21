import cv2 as cv
import numpy as np

def fun():
    filepath = "../../statics/images/imgList.tiff"
    img = cv.imread(filepath, flags=1)
    gray = cv.imread(filepath, flags=0)

    print("Ndim of img(RGB): {}, gray: {}".format(img.ndim, gray.ndim))
    print("Shape of img(RGB): {}, gray: {}".format(img.shape, gray.shape))
    print("Size of img(RGB): {}, gray: {})".format(img.size, gray.size))

    imgFloat = img.astype(np.float32) / 255
    print("Dtype of img(RGB): {}, gray: {})".format(imgFloat.dtype, gray.dtype))
    print("Dtype of imgFloat: {}".format(imgFloat.dtype))

if __name__ == '__main__':
    fun()