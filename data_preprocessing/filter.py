# Filter the OpenPose points
# The script removes NaN values, outliers and static pixels 
# corresponding to the beginning and the end of the motion. 

import os
import sys
import numpy as np
import pandas as pd
import csv

x, y, time = {}, {}, {}
x_clean, y_clean, time_clean = {}, {}, {}

# Removal of NaNs, outliers and redundant points at the start of the motion
# (works in real time and in offline mode)
def clean(x, y, time):
	start = False
	x_clean, y_clean, time_clean = [], [], []
	x_motion, y_motion, time_motion = [], [], []
	for i in range(len(x)):
		x_tmp, y_tmp, time_tmp = x[i], y[i], time[i]
		if x_tmp != 0 and y_tmp != 0:
			if len(x_clean) == 0:
				x_clean.append(x_tmp)
				y_clean.append(y_tmp)
				time_clean.append(time_tmp)
			else:
				if (abs(x_tmp - x_clean[-1]) < 20 and abs(y_tmp - y_clean[-1]) < 20):
					if len(x_clean) == 20:
						del x_clean[0], y_clean[0], time_clean[0]
					x_clean.append(x_tmp)
					y_clean.append(y_tmp)
					time_clean.append(time_tmp)
					std_x = np.std(x_clean)
					std_y = np.std(y_clean)
					if (not start) and (std_x > 2 or std_y > 2):
						print("Motion started at sample %d" %i)
						x_motion.append(x_clean[-4])
						x_motion.append(x_clean[-3])
						x_motion.append(x_clean[-2])
						y_motion.append(y_clean[-4])
						y_motion.append(y_clean[-3])
						y_motion.append(y_clean[-2])
						time_motion.append(time_clean[-4])
						time_motion.append(time_clean[-3])
						time_motion.append(time_clean[-2])
						start = True
					if (start):
						x_motion.append(x_tmp)
						y_motion.append(y_tmp)
						time_motion.append(time_tmp)
						if std_x <= 2 and std_y <= 2:
							print("Motion ended at sample %d" %i)
							return x_motion, y_motion, time_motion

# Parse the csv, call clean() and remove the 
# NaN values, outliers and static points
def read_csv(file):
    global x, y, time 
    global x_clean, y_clean, time_clean 
    
    fileName = pd.read_csv(file)
    file = file.split('/')[-1].split('.')[0]

    ## Openpose
    time = [float(str(int(item[0])) + '.' + '0'*(9-len(str(int(item[1])))) + str(int(item[1]))) \
    for item in zip(fileName['/openpose_ros/human_list/header/stamp/secs'], fileName['/openpose_ros/human_list/header/stamp/nsecs']) \
            if not np.isnan(item[0])]
    time = [i-time[0] for i in time]
    x = [i for i in fileName['/openpose_ros/human_list/human_list/0/body_key_points_with_prob/4/x'] if not np.isnan(i)]
    y = [i for i in fileName['/openpose_ros/human_list/human_list/0/body_key_points_with_prob/4/y'] if not np.isnan(i)]
    x_clean, y_clean, time_clean = clean(x, y, time)
	
    for j in range(len(x_clean)-20, 1, -1):
    	if abs(x_clean[j] - np.median(x_clean[j:len(x_clean)])) > 3 or abs(y_clean[j] - np.median(y_clean[j:len(y_clean)])) > 3:
    		break

    x_clean = x_clean[:j+3]
    y_clean = y_clean[:j+3]
    time_clean = time_clean[:j+3]

read_csv(sys.argv[1])
file = sys.argv[1].split('/')

# Save a csv with the filtered motion
csv_name = open(sys.argv[1].split('.')[0]+"_clean.csv", 'w')
wr = csv.writer(csv_name)
wr.writerow(['x', 'y', 'time'])
for i in range(len(x_clean)):
	wr.writerow([x_clean[i], y_clean[i], time_clean[i]])
csv_name.close()
