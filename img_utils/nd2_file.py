
import numpy as np
from nd2reader import ND2Reader

from . import preprocess
from .volume import Volume

class ND2File(object):
    
    def __init__(self, file_path):
        '''ND2File object initialization.'''
        
        # store path to .nd2 file
        self.file_path = file_path
        self.img_id = file_path.rstrip('.nd2')
        
        # extract and parse metadata
        self._extract_metadata()

    def load_volumes(self):
        for channel in self.channels:
            yield self.load_volume(channel)
        
    
    def load_volume(self, channel, start=None, stop=None):
        '''Loads a z-stack image in the specified channel as a 3D numpy array.'''
        
        start, stop = self._get_start_stop(start, stop)
        if not set(range(start, stop)).issubset(self.z_levels):
            raise ValueError(f'Slice [{start}:{stop}] out of range for image with {self.num_z} z-levels.')
        elif stop < start:
            raise ValueError(f'Invalid slice: [{start}:{stop}]; <start> must be less than <stop>.')

        # construct 3D volume from individual z frames
        with ND2Reader(self.file_path) as nd2_reader:
            z_frames = []
            for z in self.z_levels[start:stop]:
                z_frames.append(nd2_reader.get_frame_2D(c=channel, z=z))
        img = np.array(z_frames).astype(np.uint16)
        
        # convert intensity values to 0.0 - 1.0 space
        img = preprocess.rescale_img(img)
        
        # create a Volume object
        volume = Volume(img)
        volume.pixel_microns = self.pixel_microns
        
        # success
        return volume

    
    def _extract_metadata(self):
        '''Extracts, parses, and stores metadata from .nd2 file.'''
        
        # extract and store relevant metadata from .nd2file
        with ND2Reader(self.file_path) as nd2_reader:
            self.metadata = nd2_reader.metadata
            self.channel_names = self._clean_channel_names(self.metadata['channels'])
            self.num_channels = len(self.channel_names)
            self.channels = list(range(self.num_channels))
            self.z_levels = list(self.metadata['z_levels'])
            self.num_z = len(self.z_levels)
            self.height = self.metadata['height']
            self.width = self.metadata['height']
            self.pixel_microns = self.metadata['pixel_microns']  

    def _get_start_stop(self, start, stop):
        if start is None:
            start = np.min(self.z_levels)
        if stop is None:
            stop = np.max(self.z_levels) + 1
        return start, stop        
    
    
    def _clean_channel_names(self, channel_names):
        '''Remove spaces from channel names (e.g. 'FAR RED' --> 'FAR-RED').'''
        clean_names = [name.replace(' ', '-') for name in channel_names]
        return clean_names

    
