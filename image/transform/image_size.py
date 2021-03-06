from PyQt5.QtWidgets import QWidget, QAction

from PIL import ImageEnhance


# Action Settings
import configparser
config = configparser.ConfigParser()
config.read('config/action_settings.ini')
DOT = config['ACTION']['DOT']
SEP = config['ACTION']['SEP']
ADD = config['ACTION']['ADD']
SUB = config['ACTION']['SUB']
DIV = config['ACTION']['DIV']
MUL = config['ACTION']['MUL']
SPL = config['ACTION']['SPL']
NPZ = config['ACTION']['NPZ']
MOD = config['ACTION']['MOD']
JSN = config['ACTION']['JSN']
N = '\n'
T = '\t'
TT = '\t\t'
TTT = '\t\t\t'

class ImageSize(QWidget):
    def __init__(self, nodeflow_main, n, nn, config):
        super(ImageSize, self).__init__()

        nodeflow_main.createAttribute(node=n, name='Image_Name', preset='Image', socket=True, plug=True, dataType='img', dataAttr='')

class ImageSizeAction(QAction):
    """Model Create"""
    def __init__(self, attrData, config):
        super(ImageSizeAction, self).__init__()

        IMAGE = attrData.get('Image_Name')