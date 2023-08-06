#Imports
import json
from PIL import Image
import os
import numpy as np
import requests
from io import BytesIO
import validators

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_file_path = annotation_file
        self.transforms = transforms
     

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        '''It is reading .joson file and return number of data points'''
        with open(self.annotation_file_path) as json_file:
            data = [json.loads(line) for line in json_file]
        return len(data)

    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        with open(self.annotation_file_path) as json_file:
            data = [json.loads(line) for line in json_file]
        return data[idx]

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        image = None
        '''If url is given instead of path'''
        if(validators.url(path) == True):
            response = requests.get(path)
            image = Image.open(BytesIO(response.content))
        else:
            image = Image.open(path)
        T_list = []
        '''If there is at least one transforms object is given as argument'''
        if(self.transforms != None):
            for obj in self.transforms:
                t_img = obj.__call__(image)
                T_list.append(t_img)
        else:
            T_list.append(image)
        '''returning a list of resulted PIL image'''
        return T_list


