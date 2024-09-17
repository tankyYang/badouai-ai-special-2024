import cv2
import numpy as np

def nearet_interpolation(img):
    src_h, src_w, src_c = img.shape
    zoom = np.zeros((900, 900, src_c), np.uint8)
    k_w = 900/src_w
    k_h = 900/src_h

    for dst_y in range(900):
        for dst_x in range(900):
            src_x = int(dst_x/k_w + 0.5)
            src_y = int(dst_y/k_h + 0.5)
            zoom[dst_x, dst_y] = img[src_x, src_y]
    return zoom

if __name__ == "__main__":
    src_img = cv2.imread("lenna.png")
    dst_img = nearet_interpolation(src_img)
    cv2.imshow("dst image", dst_img)
    cv2.waitKey()
