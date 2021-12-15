#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: alf maglalang
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create a function classify_images that uses the classifier function
#          to create the classifier labels and then compares the classifier
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function
#             and as in_arg.dir for function call within main.
#            -The results dictionary as results_dic within classify_images
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main.
#           This function uses the extend function to add items to the list
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images
from classifier import classifier

# TODO 3: Define classify_images function below
#
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to
    the classifier labels, and adds the classifier label and the comparison of
    the labels to the results dictionary
    Parameters:
      images_dir - The (full) path to the folder of images
      results_dic - dict with 'key': filename and 'value': list
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match and 0 = no match
      model - Indicates which CNN model architecture: resnet alexnet vgg
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    # Process all files in the results_dic - use images_dir to give fullpath
    for key in results_dic:
        # Set model_label to be the string returned from classifier function
        model_label = classifier(images_dir + key, model)
        # model_label to lowercase without trailing and leading whitespace
        model_label = model_label.lower().strip()
        # defines truth as pet image label
        truth = results_dic[key][0]
        # extend value with model_label and the value of 1 if match or 0 if not
        if truth in model_label:
            match = 1
        else:
            match = 0
        results_dic[key].extend([model_label, match])