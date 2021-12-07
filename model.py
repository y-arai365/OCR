import cv2
import numpy as np


class Model:
    @staticmethod
    def show_img(img):
        cv2.imshow("img", img)
        cv2.waitKey()
        cv2.destroyAllWindows()

    @staticmethod
    def rot_img(img):
        img_canny = cv2.Canny(img, 50, 50)
        Model.show_img(img_canny)
        pass

    @staticmethod
    def adaptive_threshold(img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_adap = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 20)
        return img_adap

    @staticmethod
    def find_contours(img_binary):
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        return contours

    @staticmethod
    def get_rect(contour):
        center, size, deg = cv2.minAreaRect(contour)
        size = np.int0(size)
        return center, size, deg

    @staticmethod
    def rot_cut(src_img, deg, center, size):
        """傾きを整えて画像の切り取りを行う"""
        rot_mat = cv2.getRotationMatrix2D(center, deg, 1.0)
        rot_mat[0][2] += -center[0] + size[0] / 2  # -(元画像内での中心位置)+(切り抜きたいサイズの中心)
        rot_mat[1][2] += -center[1] + size[1] / 2  # 同上
        return cv2.warpAffine(src_img, rot_mat, size)
