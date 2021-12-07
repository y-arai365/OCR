"""文字列の傾きを補正する"""


class CorrectTilt:
    @staticmethod
    def binary_hsv(img):
        """黒だけを抽出するような二値化画像を取得したい"""
        pass

    @staticmethod
    def generate_character_area(img_binary):
        """文字領域の生成(文字だけがうつるような二値化画像が欲しい)"""
        pass

    @staticmethod
    def cut_character_area(img_morph):
        """膨張領域ごとに画像を切り取る"""
        pass

    @staticmethod
    def detect_corner(img_morph):
        """画像のコーナーを取得する"""
        pass
