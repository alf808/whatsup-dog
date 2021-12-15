#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#
# PROGRAMMER: alf maglalang
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create a function calculates_results_stats that calculates the
#          statistics of the results of the programrun using the classifier's model
#          architecture to classify the images.
#         This function inputs:
#            -The results dictionary as results_dic
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create
#       with this function
#
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count)
    """
    # Creates empty dictionary for results_stats_dic
    results_stats_dic = dict()
    # copy reference to results_stats_dic to shorten expressions for readability
    rsd = results_stats_dic

    # Sets all counters to initial values of zero so that they can
    # be incremented while processing through the images in results_dic
#    results_stats_dic['n_dogs_img'] = 0
#    results_stats_dic['n_match'] = 0
    rsd['n_correct_dogs'] = 0
    rsd['n_correct_notdogs'] = 0
    rsd['n_correct_breed'] = 0

    # number of total images
    rsd['n_images'] = len(results_dic)
    # process through the results dictionary
    results_vals = list(zip(*results_dic.values()))  # reorient the values
    rsd['n_match'] = sum(results_vals[2])
    rsd['n_dogs_img'] = sum(results_vals[3])
    # calculates number of not-a-dog images using - images & dog images counts
    rsd['n_notdogs_img'] = rsd['n_images'] - rsd['n_dogs_img']
    # iterate through results_dic to check count of correct breed, correct dogs, correct non-dogs
    for key in results_dic:
        if results_dic[key][2]+results_dic[key][3] == 2:
            rsd['n_correct_breed'] += 1
        if results_dic[key][3]+results_dic[key][4] == 2:
            rsd['n_correct_dogs'] += 1
        if results_dic[key][3]+results_dic[key][4] == 0:
            rsd['n_correct_notdogs'] += 1
    # calculate percentages based on counts above

    try:
        rsd['pct_correct_dogs'] = rsd['n_correct_dogs'] / rsd['n_dogs_img'] * 100
        rsd['pct_correct_breed'] = rsd['n_correct_breed'] / rsd['n_dogs_img'] * 100
        rsd['pct_match'] = rsd['n_match'] / rsd['n_images'] * 100  # optional
        if rsd['n_notdogs_img'] > 0:
            rsd['pct_correct_notdogs'] = rsd['n_correct_notdogs'] / rsd['n_notdogs_img'] * 100
        else:
            rsd['pct_correct_notdogs'] = 0.0
    except ZeroDivisionError as e:
        print(f'Please check if you have images in the path or folder. {e}')

    return results_stats_dic