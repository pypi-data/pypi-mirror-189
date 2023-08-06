#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size, relative = False):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
            if relative is False it will do above things.
            if it is True it scale original image to x(output_size)
        '''
        self.output_size = output_size
        self.relative = relative

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        op_size = self.output_size
        if(self.relative == False):
            '''If given argument is a single integer'''
            if(isinstance(op_size, int)):
                w, h = image.size
                new_size = None
                '''Finding tuple for new size'''
                if(w < h):
                    new_size = (op_size, (op_size*h)//w)
                else:
                    new_size = ((op_size*w)//h, op_size)
                res_img = image.resize(new_size)
                return res_img
            else:
                res_img = image.resize(op_size)
                return res_img
        else:
            w, h = image.size
            new_size = (int(w*op_size), int(h*op_size))
            res_img = image.resize(new_size)
            return res_img