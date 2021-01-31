# Create labeled data

## Description
The goal is to create labeled data. Two types of datasets were created:

* x-y dataset: Contains the x-y pixels of the movement and a number (1-5) as the Class label pertaining to the position of the object

* w-b dataset: Used the x-y pixels and a Linear Square Estimator (LSE) to fit a line to the motion of the human. For each movement, we used a window of increasing length to determine which x-y pixels will be used as an input to the LSE. The dataset contains the w,b coefficients of the various lines and a number (1-5) as the Class label.

## Files

* xy_creation.py: A Python script for creating the x-y dataset.

* wb_creation.py: A Python script for creating the w-b dataset.

* real_time_linear_regression_model.py: A Python script which utilizes the Dash library for real time visualization of the LSE model and the generation of the w,b coefficients.




