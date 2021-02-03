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

## Brief results
In the following figure, the accuracy scores for the 22Hz are shown
<img src="https://github.com/ThanasisTs/object_direction_prediction/blob/main/classifiers/xy_classifiers/accuracy_real_time.png" >

An accuracy of around 80% is achieved using Decision trees and Naive Bayes classifiers when 4 pixels are obtained. Taking into account the OpenPose frequency (22Hz), this indicates that a correct prediction with accuracy 80% is achieved approximately at the first 188ms of the human motion. SVM's performance is much more poor compared to the other two.

In the following figure, the accuract scores for the 60Hz are shown
<img src="https://github.com/ThanasisTs/object_direction_prediction/blob/main/classifiers/xy_classifiers/accuracy_all_frames.png">

An accuracy of around 80% is achieved using Decision trees and Naive Bayes classifiers when 7 pixels are obtained. This indicates that a corrept predition with accuracy 80% is achieved approximately at the first 117ms of the human motion. SVM achieves such level of accuracy at 17 pixels or at 283ms.

