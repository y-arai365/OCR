import cv2
import numpy as np
import os
from PIL import Image
import pyocr.builders


class Controller:
    def __init__(self, path, model, correct_tilt):
        self.model = model
        self.correct_tilt = correct_tilt
        self.img_origin = cv2.imread(path)

        self.my_func()

    def my_func(self):
        # インストール済みのTesseractのパスを通す
        path_tesseract = r"C:\Program Files\Tesseract"
        if path_tesseract not in os.environ["PATH"].split(os.pathsep):
            os.environ["PATH"] += os.pathsep + path_tesseract
        # self.model.show_img(self.img_origin)

        img_adap = self.model.adaptive_threshold(self.img_origin)
        self.model.show_img(img_adap)

        kernel = np.ones((5, 25), np.uint8)
        img_morph = cv2.morphologyEx(img_adap, cv2.MORPH_OPEN, kernel)
        self.model.show_img(img_morph)

        for j in range(len(self.img_origin)):
            for i in range(len(self.img_origin[0])):
                if img_adap[j][i] == 255:
                    self.img_origin[j][i] = np.array((255, 255, 255))
        self.model.show_img(self.img_origin)

        contours = self.model.find_contours(img_morph)
        for contour in contours:
            center, size, deg = self.model.get_rect(contour)
            print(size)
            if 20 < size[0] < 460 and 20 < size[1] < 460:
                img_con = self.model.rot_cut(self.img_origin, deg, center, size)
                self.model.show_img(img_con)


        # OCRエンジンの取得
        tools = pyocr.get_available_tools()
        tool = tools[0]

        # c_max = 169
        # for j in range(len(self.img_origin)):
        #     for i in range(len(self.img_origin[0])):
        #         if self.img_origin[j][i][0] > c_max or self.img_origin[j][i][1] > c_max or self.img_origin[j][i][2] > c_max:
        #             # print(self.img_origin[i][j])
        #             self.img_origin[j][i] = np.array((255, 255, 255))
        # self.model.show_img(self.img_origin)

        # pil_image = Image.fromarray(self.img_origin)
        pil_image = Image.fromarray(img_morph)
        # ＯＣＲ実行
        builder = pyocr.builders.TextBuilder()
        result = tool.image_to_string(pil_image, lang="jpn", builder=builder)

        print(result)
