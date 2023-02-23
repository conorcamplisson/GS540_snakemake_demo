
import numpy as np

from .image import Image

class Volume(object):
    
    def __init__(self, img):
        self.img = img
        self.num_z = img.shape[0]
        self.z_levels = list(range(self.num_z))
        self.height = img.shape[1]
        self.width = img.shape[2]
        self.pixel_microns = None
            

    def max_project(self, start=None, stop=None):
        start, stop = self._get_start_stop(start, stop)
        max_img = Image(np.max(self.img[start:stop,:,:], axis=0))
        max_img.pixel_microns = self.pixel_microns
        return max_img
    
    
    def plot_max_z(self, start=None, stop=None, autoscale=False):
        max_img = self.max_project(start, stop)
        if autoscale:
            max_img.autoscale()        
        max_img.show()
        return max_img
        
    
    def _get_start_stop(self, start, stop):
        if start is None:
            start = np.min(self.z_levels)
        if stop is None:
            stop = np.max(self.z_levels) + 1
        return start, stop        
        
    
    def __str__(self):
        return f'<Volume: {self.num_z} z-levels ({self.width} x {self.height})>'
    def __repr__(self):
        return self.__str__()

