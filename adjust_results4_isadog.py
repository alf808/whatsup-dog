#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#
# PROGRAMMER: alf maglalang
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results
#          dictionary to indicate whether or not the pet image label is of-a-dog,
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the
#          dog name (from dognames.txt) and the 'value' is one. If a label is
#          found to exist within this dictionary of dog names then the label
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog.
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main.
#
##
# TODO 4: Define adjust_results4_isadog function below
#
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
                    List. Where the list will contain the following items:
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 where 1: 'is-a' dog and 0: 'is-NOT-a' dog.
                 NEW - index 4 = 1/0 where 1 = Classifier as-a-dog and 0 'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files.
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    dognames_dic = dict()
    # Reads in dognames from file
    with open(dogfile) as infile:
        # Reads in dognames from first line in file
        line = infile.readline().strip()
        while line:
            # check if the dogname(line) exists in dognames_dic. if not, add the
            # dogname(line) to dognames_dic as the 'key' with the 'value' of 1
            if line not in dognames_dic:
                dognames_dic[line] = 1
            line = infile.readline().strip()
    # iterate through results_dic. if labels are found in dognames_dic
    # then label "is a dog" index3/4=1 otherwise index3/4=0 "not a dog"
    for key in results_dic:
        is_pet_label_dog, is_class_dog = 0, 0
        if results_dic[key][0] in dognames_dic:
            is_pet_label_dog = 1
            if results_dic[key][1] in dognames_dic:
                is_class_dog = 1
        else:
            if results_dic[key][1] in dognames_dic:
                is_class_dog = 1
        results_dic[key].extend([is_pet_label_dog, is_class_dog])