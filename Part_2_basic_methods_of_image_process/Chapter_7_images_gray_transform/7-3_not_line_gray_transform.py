import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def logarithmic_transform():
    gray = cv.imread("../../statics/images/Fig0602.png", flags=0)

    fft = np.fft.fft2(gray)  # 傅里叶变换
    fft_shift = np.fft.fftshift(fft)  # 将低频部分移动到图像中心
    amp = np.abs(fft_shift)  # 傅里叶变换的频谱
    ampNorm = np.uint8(cv.normalize(amp, None, 0, 255, cv.NORM_MINMAX))

    ampLog = np.abs(np.log(1.0 + np.abs(fft_shift)))
    ampLogNorm = np.uint8(cv.normalize(ampLog, None, 0, 255, cv.NORM_MINMAX))

    plt.figure(figsize=(9, 3.2))

    plt.subplot(131), plt.title("1. original"), plt.axis('off')
    plt.imshow(gray, cmap='gray', vmin=0, vmax=255)

    plt.subplot(132), plt.title("2. FFT"), plt.axis('off')
    plt.imshow(ampNorm, cmap='gray', vmin=0, vmax=255)

    plt.subplot(133), plt.title("3. Log"), plt.axis('off')
    plt.imshow(ampLogNorm, cmap='gray', vmin=0, vmax=255)

    plt.tight_layout()
    plt.show()

def gamma_transform():
    gray = cv.imread("../../statics/images/Fig0701.png", flags=0)

    c = 1
    gammas = [0.25, 0.5, 1.0, 1.5, 2.0, 4.0]
    fig = plt.figure(figsize=(9, 5.5))
    for i in range(len(gammas)):
        ax = fig.add_subplot(2, 3, i + 1, xticks=[], yticks=[])
        img_gamma = c * np.power(gray, gammas[i])  # 伽马变换
        ax.imshow(img_gamma, cmap='gray')
        if gammas[i] == 1.0:
            ax.set_title("1. original")
        else:
            ax.set_title(f"{gammas[i]}")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # gamma_transform()
    logarithmic_transform()