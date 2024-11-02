import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def levelsAdjust(img, Sin=0, Hin=255, Mt=1.0, Sout=0, Hout=255):
    Sin = min(max(Sin, 0), Hin - 2)
    Hin = min(Hin, 255)
    Mt = min(max(Mt, 0.01), 9.99)
    Sout = min(max(Sout, 0), Hout - 2)
    Hout = min(Hout, 255)
    difin = Hin - Sin
    difout = Hout - Sout
    table = np.zeros(256, np.uint16)
    for i in range(256):
        V1 = min(max(255 * (i - Sin) / difin, 0), 255)
        V2 = 255 * np.power( (V1 / 255), Mt)
        table[i] = min(max(Sout + difout * V2 / 255, 0), 255)
    imgTone = cv.LUT(img, table)
    return imgTone

# 自动调整色阶
def autoLevels(gray, cutoff=0.1):
    table = np.zeros((1, 256), np.uint8)
    # cutoff=0.1, 计算 0.1%, 99.9% 分位的灰度值
    low = np.percentile(gray, q=cutoff)  # cutoff=0.1, 0.1 分位的灰度值
    high = np.percentile(gray, q=100 - cutoff)  # 99.9 分位的灰度值, [0, high] 占比99.9%
    # 输入动态线性拉伸
    Sin = min(max(low, 0), high - 2)  # Sin, 黑场阈值, 0<=Sin<Hin
    Hin = min(high, 255)  # Hin, 白场阈值, Sin<Hin<=255
    difIn = Hin - Sin
    V1 = np.array([(min(max(255 * (i - Sin) / difIn, 0), 255)) for i in range(256)])
    # 灰场伽马调节
    gradMed = np.median(gray)  # 拉伸前的中值
    Mt = V1[int(gradMed)] / 128.  # 拉伸后的映射值
    V2 = 255 * np.power(V1 / 255, 1 / Mt)  # 伽马调节
    # 输出线性拉伸
    Sout, Hout = 5, 250  # Sout 输出黑场阈值, Hout 输出白场阈值
    difOut = Hout - Sout
    table[0, :] = np.array([(min(max(Sout + difOut * V2[i] / 255, 0), 255)) for i in range(256)])
    return cv.LUT(gray, table)


if __name__ == '__main__':
    gray = cv.imread("../../statics/images/Lena.tif", 0)
    print("cutoff={},minG={},maxG={}".format(0.0, gray.min(), gray.max()))

    # 色阶手动调整
    equManual = levelsAdjust(gray, 64, 200, 1.5, 0, 255)
    cutoff = 0.1
    equAuto = autoLevels(gray, cutoff)

    plt.figure(figsize=(9, 3.5))
    plt.subplot(131), plt.title("1. origin"), plt.axis('off')
    plt.imshow(cv.cvtColor(gray, cv.COLOR_BGR2RGB))
    plt.subplot(132), plt.title("2. Manual"), plt.axis('off')
    plt.imshow(cv.cvtColor(equManual, cv.COLOR_BGR2RGB))
    plt.subplot(133), plt.title("3. Auto"), plt.axis('off')
    plt.imshow(cv.cvtColor(equAuto, cv.COLOR_BGR2RGB))
    plt.tight_layout()
    plt.show()


