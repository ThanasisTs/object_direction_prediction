# Prediction

## Training - Testing datasets

* Train using 60Hz dataset and test in 60Hz dataset
* Train using 22Hz dataset and test in 22Hz dataset

<b>NOTE:</b> For the rest of the text, `all_frames` pertains to the dataset @ 60Hz and `real_time` to the dataset @ 22Hz.

We first split the data into training/validation and testing datasets. The testing dataset consisted of 15% of the total dataset. That applied to both `all_frames` and `real_time` datasets. Once we observed the results in the validation set, we trained the classifiers using both the training and the validation sets and used the testing set for the final evaluation.

## Classifiers
Three classifiers were used for the prediction: Naive Bayes, Decision Tree and SVM. For each classifier we used the `KFold` function of `sklearn` to get different combinations of training and validation datasets. The number of splits was set to 10. For the SVM classifier, a linear kernel and C=1 was used after exprerimenting with the hyperparemeters. For the kernel, we compared the rbf and the linear kernel and for the C we used the values 0.1, 1 and 10.

## Experiments
To simulate a real-time behaviour, we assumed that the pixels of a trajectory are not available at once but they are obtained over time. The prediction was made based on the number of available pixels. For that reason, a window of increasing length was considered and the number of pixels inside the window were considered the current feature vector.

## Evaluation
To compare the three classifiers, we used the `accuracy_score` and the `confusion_matrix` metrics. The `accuracy_score` was used to observe their overall performance and to compare the algorithms with respect to time, namely at which time during the human motion the prediction exceeded a predetermined threshold. The `confustion_matrix` was used to observe the behaviour of the classifiers along each class.

## Files
* <b> training: </b> Training and validation of the classifiers
* <b> testing: </b> Testing of the classifiers
* <b> models: </b> Stored models used in the testing
* <b> csvs: </b> CSVs containing the accuracy scores for the validation and the testing
* <b> figs: </b> Figures of the accuracy and plots of the confusion matrices

## Results

### Validation
We first present the results in the validation.

In the following figure, the accuracy scores for the `real_time` dataset are shown
<img src="https://github.com/ThanasisTs/object_direction_prediction/blob/main/classifiers/xy_classifiers/figs/accuracy_real_time.png" >

An accuracy of around 80% is achieved using Decision trees and Naive Bayes classifiers when 4 pixels are obtained. Taking into account the OpenPose frequency (22Hz), this indicates that a correct prediction with accuracy 80% is achieved approximately at the first 188ms of the human motion. SVM achieves the same accuracy level at 3 pixels, indicating an 80% prediction at the first 136ms.

In the following figure, the accuracy scores for the `all_frames` dataset are shown
<img src="https://github.com/ThanasisTs/object_direction_prediction/blob/main/classifiers/xy_classifiers/figs/accuracy_all_frames.png">

An accuracy of around 80% is achieved using Decision trees and Naive Bayes classifiers when 7 pixels are obtained. This indicates that a corrept predition with accuracy 80% is achieved approximately at the first 117ms of the human motion. SVM on the other hand achieves an accuracy of 90% at the first 5 pixels leading to an accuracy of that level at the first 83ms.

The results indicate that SVM results in the highest accuracy. Furthermore, having available the pixels at 60Hz instead of 22Hz results in approximately 1.5 times faster prediction.

### Testing

In the following figure, the accuracy scores for the `real_time` dataset are shown
<img src="https://github.com/ThanasisTs/object_direction_prediction/blob/main/classifiers/xy_classifiers/figs/accuracy_real_time.png" >

An accuracy of around 80% is achieved using Decision trees and Naive Bayes classifiers when 4 pixels are obtained. Taking into account the OpenPose frequency (22Hz), this indicates that a correct prediction with accuracy 80% is achieved approximately at the first 188ms of the human motion. SVM achieves the same accuracy level at 3 pixels, indicating an 80% prediction at the first 136ms.

In the following figure, the accuracy scores for the `all_frames` dataset are shown
<img src="https://github.com/ThanasisTs/object_direction_prediction/blob/main/classifiers/xy_classifiers/figs/accuracy_all_frames.png">

An accuracy of around 80% is achieved using Decision trees and Naive Bayes classifiers when 7 pixels are obtained. This indicates that a corrept predition with accuracy 80% is achieved approximately at the first 117ms of the human motion. SVM on the other hand achieves an accuracy of 90% at the first 5 pixels leading to an accuracy of that level at the first 83ms.

The results indicate that SVM results in the highest accuracy. Furthermore, having available the pixels at 60Hz instead of 22Hz results in approximately 1.5 times faster prediction.

