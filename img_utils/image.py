
import numpy as np

from . import plotting

class Image(object):
    
    def __init__(self, img):
        self.img = img
        self.height = img.shape[0]
        self.width = img.shape[1]
        self.pixel_microns = None
        
    def show(self):
        plotting.show_img(self.img)

