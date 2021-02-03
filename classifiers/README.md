# Classifiers

## Description
Three classifiers were used for the prediction. Naive Bayes, Decision Tree and SVM

## Files

* xy_classifiers: Classifiers for the xy_dataset
* wb_classifiers: Classifiers for the wb_dataset

## Training - Testing datasets

* Train using 60Hz dataset and test in 60Hz dataset
* Train using 60Hz dataset and test in 22Hz (OpenPose frequency) dataset
* Train using 22Hz dataset and test in 22Hz dataset

## Classification

For each classifier we used the `KFold` function of `sklearn` to get different combinations of training and validation datasets. The number of splits was set to 10. To get the best instance for each classifier, we used the `accuracy_score` as a metric and chose the instance which resulted in the best accuracy. That instance was then used in the testing dataset.

## Comparison
To compare the three classifiers, we used the `accuracy_score` and the `confusion_matrix` metrics. The `accuracy_score` was used to compare the algorithms with respect to the time, namely at which time along the human motion the prediction exceeded a predetermined threshold. The `confustion_matrix` was used to observe the behaviour of the classifiers along each class.

## Run
`python <classifier>.py <file>`
* classifier: decision_tree_classifier.py, naive_bayes_classifier.py, svm_classifier.py
* file: all_frames.csv (60Hz), real_time.csv(22Hz)

In the following figure, the accuracy scores for the 22Hz are shown

In the following figure, the accuract scores for the 60Hz are shown
