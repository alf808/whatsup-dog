# Image Classification for a City Dog Show
## Project Goal
In this project, you will use a created image classifier to identify dog breeds.
## Description:
Your city is hosting a citywide dog show and you have volunteered to help the organizing committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog.
## Your Tasks:
    • determine which image classification algorithm works the "best" on classifying images as "dogs" or "not dogs".
    • Determine how well the "best" classification algorithm works on correctly identifying a dog's breed.
    • Time how long each algorithm takes to solve the classification problem. With computational tasks, there is often a trade-off between accuracy and runtime. The more accurate an algorithm, the higher the likelihood that it will take more time to run and use more computational resources to run.

Important Notes:
For this image classification task, you will be implementing an image classification application using a deep learning model called a convolutional neural network (often abbreviated as CNN). CNNs work particularly well for detecting features in images like colors, textures, and edges; then using these features to identify objects in the images. You'll use a CNN that has already learned the features from a giant dataset of 1.2 million images called ImageNet. There are different types of CNNs that have different structures (architectures) that work better or worse depending on your criteria. With this project, you'll explore the three different architectures (AlexNet, VGG, and ResNet) and determine which is best for your application.
The test_classifier.py file contains an example program that demonstrates how to use the classifier function.
Remember that certain breeds of dogs look very similar. The more images of two similar-looking dog breeds that the algorithm has learned from, the more likely the algorithm will be able to distinguish between those two breeds.

## Project Instructions
### Principal Objectives
    1. Correctly identify which pet images are of dogs (even if the breed is misclassified) and which pet images aren't of dogs.
    2. Correctly classify the breed of dog, for the images that are of dogs.
    3. Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve objectives 1 and 2.
    4. Consider the time resources required to best achieve objectives 1 and 2, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms takes to run.

Create the program file that will achieve the four objectives above.
    • Function docstrings contain input parameters and return values, which were left to provide guidance. You are welcome to program these functions differently.
    • In 6. Timing Code to 19. programming the undefined functions and completing program.
    • You can use the functions within the program print_functions_for_lab_checks.py to check your code for sections 8. Command Line Arguments through 17. Calculating Results. You will find this program within the Project Workspace.
Program Outline
    • Time your program
        ◦ Use Time Module to compute program runtime
    • Get program Inputs from the user
        ◦ Use command line arguments to get user inputs
    • Create Pet Images Labels
        ◦ Use the pet images filenames to create labels
        ◦ Store the pet image labels in a data structure (e.g. dictionary)
    • Create Classifier Labels and Compare Labels
        ◦ Use the Classifier function to classify the images and create the classifier labels
        ◦ Compare Classifier Labels to Pet Image Labels
        ◦ Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g. dictionary of lists)
    • Classifying Labels as "Dogs" or "Not Dogs"
        ◦ Classify all Labels as "Dogs" or "Not Dogs" using dognames.txt file
        ◦ Store new classifications in the complex data structure (e.g. dictionary of lists)
    • Calculate the Results
        ◦ Use Labels and their classifications to determine how well the algorithm worked on classifying images
    • Print the Results
These tasks will be repeated for each of the three image classification algorithms.

### Results
In this section, we
    • Provide the results from running the check_images.py for all three CNN model architectures
    • Compare these results to the ones your program produced when you ran run_models_batch.sh (or run_models_batch_hints.sh) in the Printing Results section
    • Discuss how the four primary objectives
In this project we had 2 main objectives:
    1. Identifying which pet images are of dogs and which pet images aren't of dogs
    2. Classifying the breeds of dogs, for the images that are of dogs
This program should provide with objectives 1 and 2 when it was run. In the table below, you will find oresults for each of the model architectures.
    • For objective 1, notice that both VGG and AlexNet correctly identify images of "dogs" and "not-a-dog" 100% of the time.
    • For objective 2, VGG provides the best solution because it classifies the correct breed of dog over 90% of the time.
### Results Table

Project Results
Given our results, the "best" model architecture is VGG. It outperformed both of the other architectures when considering both objectives 1 and 2. You will notice that ResNet did classify dog breeds better than AlexNet, but only VGG and AlexNet were able to classify "dogs" and "not-a-dog" at 100% accuracy. The model VGG was the one that was able to classify "dogs" and "not-a-dog" with 100% accuracy and had the best performance regarding breed classification with 93.3% accuracy.
Use the next (last!) workspace to present and print your final results. You can use the table above as a reference.
