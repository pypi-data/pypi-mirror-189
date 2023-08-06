#Imports
from PIL import Image
import random

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        width, height = image.size
        if(self.crop_type == 'center'):
            '''Finding corner points of cropped image'''
            left = (width/2 - self.shape[1]/2)
            right = (width/2 + self.shape[1]/2)
            top = (height/2 - self.shape[0]/2)
            bottom = (height/2 + self.shape[0]/2)
            crpd_img = image.crop((left, top, right, bottom))
            return crpd_img
        if(self.crop_type == 'random'):
            matrix_h = self.shape[0]
            matrix_w = self.shape[1]
            '''Generating random valid corner point for croppings'''
            x1 = random.randrange(0, width - matrix_w)
            y1 = random.randrange(0, height - matrix_h)
            crpd_img = image.crop((x1, y1, x1 + matrix_w, y1 + matrix_h))
            return crpd_img