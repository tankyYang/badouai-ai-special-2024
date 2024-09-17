import cv2
import numpy as np

def map_dst_to_src(dst, scale):
    return (dst + 0.5) * scale - 0.5


def bilinear_interpolation(img, out_dim):
    src_h, src_w , src_c = img.shape
    dst_h, dst_w = out_dim[1], out_dim[0]
    if dst_h == src_h and dst_w == src_w:
        return img.copy()

    dst_img = np.zeros((dst_h, dst_w, src_c), np.uint8)
    scale_x = float(src_w) / dst_w
    scale_y = float(src_h) / dst_h
    for i in range(src_c):
        for dst_x in range(dst_w):
            for dst_y in range(dst_h):
                src_x = map_dst_to_src(dst_x, scale_x)
                src_y = map_dst_to_src(dst_y, scale_y)

                #find four Q point
                q_x0 = int(src_x)
                q_x1 = min(q_x0+1, src_w-1)
                q_y0 = int(src_y)
                q_y1 = min(q_y0+1, src_h-1)

                temp0 = (q_x1 - src_x) * img[q_y0, q_x0, i] + (src_x - q_x0) * img[q_y0, q_x1, i]
                temp1 = (q_x1 - src_x) * img[q_y1, q_x0, i] + (src_x - q_x0) * img[q_y1, q_x1, i]
                dst_img[dst_y, dst_x, i] = int((q_y1 - src_y) * temp0 + (src_y - q_y0) * temp1)

    return dst_img


if __name__ == "__main__":
    img = cv2.imread("lenna.png")
    dst = bilinear_interpolation(img, (700, 700))
    cv2.imshow("bilinear_interpolation", dst)
    cv2.waitKey()
