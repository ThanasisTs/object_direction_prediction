# Object direction prediction

## Description
Let us assume that there are 5 objects on a table and a human approaches one of them. The goal of this project is the prediction of the object that the human tries to approach. Human monitoring is achieved using a RGB-D camera. The objects are placed in known locations and therefore no object detection or object localization algorithms are used.

## Files

* <b> data_collection:</b> Description of the human data collection procedure and the human motion representation.
* <b> data_preprocessing:</b> Preprocessing steps of the collected data.
* <b> train_test_datasets:</b> Creation of the datasets used in the training and the testing. CSVs with the datasets.
* <b> learning:</b> Python implementation of the training and testing procedure. Presentation of the results of the learning.
* <b> ML_Presentation.pdf:</b> Pdf of the presentation.

## Python modules versions

* numpy: 1.19.5
* pandas: 1.1.4
* sklearn: 0.0
* seaborn: 0.11.0
* matplotlib: 3.3.2
* plotly: 4.14.1
