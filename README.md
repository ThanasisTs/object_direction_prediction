# Object direction prediction

## Description
Suppose that there are several objects upon a table and a human a human who wants
to clean it. The goal of this project is the prediction of the object that the human tries
to approach. We suppose that the objects are placed in known locations.

## Human motion
An RGB-D camera is employed for the human monitoring and the human motion acquitision is based on 
[Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), which is a 2D human pose estimation
framework. The human motion corresponds to the motion of the right wrist.

## Input preprocessing
An Openpose trajectory consists of x-y RGB pixels. The preprocessing procedure removes NaN values
(originated from frames in which the human wrist was not localized), outliers (originated from frames in which
the human wrist was incorrectly localized) and redundant values (originated from frames in which the human was
stasionary).

<img src="https://github.com/ThanasisTs/object_direction_prediction/blob/main/openpose.png" width="800" height="400">
<img src="https://github.com/ThanasisTs/object_direction_prediction/blob/main/keypoints.png" width="800" height="400">

