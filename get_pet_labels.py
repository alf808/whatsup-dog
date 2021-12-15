#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: alf maglalang
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import re

# TODO 2: Define get_pet_labels function below
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Parameters:
     image_dir - The (full) path to the folder of images
    Returns:
      results_dic - dict with 'key': filename string and 'value': list
    """
    results_dic = dict()
    temp_files = listdir(image_dir)  # list of filenames
    # Eliminate file names that do NOT begin with alphabetic character
    filenames = [file for file in temp_files if re.match('^[a-zA-Z]', file)]
    pet_labels = [label.lower().split('_') for label in filenames]
    # Process through each label extracting only alpha words
    for idx, label in enumerate(pet_labels):
        pet_label = [item.strip() for item in label if item.isalpha()]
        pet_labels[idx] = ' '.join(pet_label)
    # eliminate duplicate filenames before inserting into dictionary
    for idx in range(len(filenames)):
        if filenames[idx] not in results_dic:
            results_dic[filenames[idx]] = [pet_labels[idx]]
        else:
            print("** Warning: Key=", filenames[idx],
                  "already exists in results_dic with value =",
                  results_dic[filenames[idx]])
    return results_dic

if __name__ == '__main__':
    pet_dict = get_pet_labels('pet_images/')
    print(pet_dict)
    print(len(pet_dict))