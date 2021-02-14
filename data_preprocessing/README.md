# Data preprocessing

## Description
The preprocessing step contains:
* <b>NaN values removal:</b> NaN values correspond to frames where the human wrist was not localized.
* <b>Outlier removal:</b> Outliers correspond to frames where the human wrist was incorrectly localized. To check for outliers we computed the distance of consecutive pixels in each axis and if this distance was greater than 20 pixels in any axis, then the second pixel was considered outlier. The value of 20 pixels was chosen experimentally.
  * <b>Static pixels removal:</b> Static pixels are considered the pixels which correspond to the station of the human either before starting moving or after having completed his motion. These pixels do not contain any information regarding the object location and for the prediction are considered redundant.

## Files
* `filter.py`: A Python script for removing NaN values, outliers and static pixels and for creating a CSV file containing the data of the clean motion.
* `filter`: A bash script for running `filter.py` for all human movements.
