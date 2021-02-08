# Classifiers

## Description
Three classifiers were used for the prediction. Naive Bayes, Decision Tree and SVM

## Training - Testing datasets

* Train using 60Hz dataset and test in 60Hz dataset
* Train using 22Hz dataset and test in 22Hz dataset

## Classification

For each classifier we used the `KFold` function of `sklearn` to get different combinations of training and validation datasets. The number of splits was set to 10.

## Experiments
To simulate a real-time behaviour, we assumed that the pixels of a trajectory are not available at one time but they are obtained over time. The prediction was made based on the number of available pixels. For that reason, a sliding window of increasing length was considered and the number of pixels inside the window were considered the current feature vector.

## Comparison
To compare the three classifiers, we used the `accuracy_score` and the `confusion_matrix` metrics. The `accuracy_score` was used to compare the algorithms with respect to the time, namely at which time along the human motion the prediction exceeded a predetermined threshold. The `confustion_matrix` was used to observe the behaviour of the classifiers along each class.

## Run
`python <classifier>.py <file>`
* classifier: decision_tree_classifier.py, naive_bayes_classifier.py, svm_classifier.py
* file: all_frames.csv (60Hz), real_time.csv (22Hz)

## Results
In the following figure, the accuracy scores for the 22Hz are shown
<img src="https://github.com/ThanasisTs/object_direction_prediction/blob/main/classifiers/xy_classifiers/figs/accuracy_real_time.png" >

An accuracy of around 80% is achieved using Decision trees and Naive Bayes classifiers when 4 pixels are obtained. Taking into account the OpenPose frequency (22Hz), this indicates that a correct prediction with accuracy 80% is achieved approximately at the first 188ms of the human motion. SVM achieves the same accuracy level at 3 pixels, indicating an 80% prediction at the first 136ms.

In the following figure, the accuract scores for the 60Hz are shown
<img src="https://github.com/ThanasisTs/object_direction_prediction/blob/main/classifiers/xy_classifiers/figs/accuracy_all_frames.png">

An accuracy of around 80% is achieved using Decision trees and Naive Bayes classifiers when 7 pixels are obtained. This indicates that a corrept predition with accuracy 80% is achieved approximately at the first 117ms of the human motion. SVM on the other hand achieves an accuracy of 90% at the first 5 pixels leading to an accuracy of that level at the first 83ms.

The results indicate that SVM results in the highest accuracy. Linear kernel and C=1 was used after exprerimenting with the hyperparemeters. Furthermore, having available the pixels at 60Hz instead of 22Hz results in approximately 1.5 times faster prediction.

