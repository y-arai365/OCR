from model import Model
from controller import Controller
from correct_tilt import CorrectTilt


path = r"./card_image/camera_capture_18.jpg"
m = Model()
ct = CorrectTilt()
c = Controller(path, model=m, correct_tilt=ct)
