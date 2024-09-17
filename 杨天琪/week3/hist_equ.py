import  cv2
import numpy as np
from matplotlib import pyplot as plt

def hist_equal(src_img):
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    dst = cv2.equalizeHist(gray)
    hist = cv2.calcHist([dst], [0], None, [256], [0, 256])

    plt.figure()
    plt.hist(dst.ravel(), 256)
    plt.show()
    return dst



if __name__ == "__main__":
    src_img = cv2.imread("lenna.png")
    hist = hist_equal(src_img)
    cv2.imshow("hist euqal", hist)
    cv2.waitKey()
