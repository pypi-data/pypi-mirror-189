from PIL import Image
import requests
from io import BytesIO


class Download(object):
    '''
        A class for helping in dowloading the required images from the given url to the specified path
    '''

    '''I have added a new argument of image name for saving it'''
    def __call__(self, path, url, name):
        '''
            Arguments:
            path: download path with the file name
            url: required image URL
            name : name of the saved image
        '''
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.save(f"{path}/{name}")

