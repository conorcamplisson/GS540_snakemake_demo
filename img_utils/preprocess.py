import numpy as np
from skimage import exposure

def rescale_img(img, vmin=0.0, vmax=1.0):
    '''TODO...'''

    # infer max potential pixel intensity from image type
    if img.dtype == np.uint8:
        max_val = 2**8 - 1
    elif img.dtype == np.uint16:
        max_val = 2**16 - 1
    else:
        raise NotImplementedError('TODO - need to handle img of dtype', img.dtype)
    
    # rescale intensity values
    rescaled = exposure.rescale_intensity(img, (0, max_val), (vmin, vmax))

    # success
    return rescaled

