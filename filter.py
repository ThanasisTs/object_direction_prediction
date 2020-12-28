# Filter the Openpose trajectories
# The script removes NaNs, outliers and redundant points corresponding to the beginning
# and the end of the motion. 

import os
import sys
import numpy as np
import pandas as pd
import plotly
import plotly.offline as py
import plotly.graph_objects as go
import csv

openpose_x, openpose_y, openpose_time = {}, {}, {}
openpose_x_clean, openpose_y_clean, openpose_time_clean = {}, {}, {}

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

# Parse the csv, call clean() and remove the redundant points at the end of the motion
# (the removal at the end of the motin does NOT work in real-time)
def read_csv(file):
    global openpose_x, openpose_y, openpose_time 
    global openpose_x_clean, openpose_y_clean, openpose_time_clean 
    
    fileName = pd.read_csv(file)
    file = file.split('/')[-1].split('.')[0]

    ## Openpose
    openpose_time = [float(str(int(item[0])) + '.' + '0'*(9-len(str(int(item[1])))) + str(int(item[1]))) \
    for item in zip(fileName['/openpose_ros/human_list/header/stamp/secs'], fileName['/openpose_ros/human_list/header/stamp/nsecs']) \
            if not np.isnan(item[0])]
    openpose_time = [i-openpose_time[0] for i in openpose_time]
    openpose_x = [i for i in fileName['/openpose_ros/human_list/human_list/0/body_key_points_with_prob/4/x'] if not np.isnan(i)]
    openpose_y = [i for i in fileName['/openpose_ros/human_list/human_list/0/body_key_points_with_prob/4/y'] if not np.isnan(i)]
    openpose_x_clean, openpose_y_clean, openpose_time_clean = clean(openpose_x, openpose_y, openpose_time)
	
    for j in range(len(openpose_x_clean)-20, 1, -1):
    	if abs(openpose_x_clean[j] - np.median(openpose_x_clean[j:len(openpose_x_clean)])) > 3 or abs(openpose_y_clean[j] - np.median(openpose_y_clean[j:len(openpose_y_clean)])) > 3:
    		break

    openpose_x_clean = openpose_x_clean[:j+3]
    openpose_y_clean = openpose_y_clean[:j+3]
    openpose_time_clean = openpose_time_clean[:j+3]

# Runs locally
read_csv(sys.argv[1])
file = sys.argv[1].split('/')

# Save a csv with the filtered motion
os.chdir("/home/thanasis/MSC_AI/Machine_Learning/assignment/csvs_clean/"+file[-3]+"/"+file[-2])
csv_name = open(sys.argv[1].split('/')[-1].split('.')[0]+'.csv', 'w')
wr = csv.writer(csv_name)
wr.writerow(['x', 'y', 'time'])
for i in range(len(openpose_x_clean)):
	wr.writerow([openpose_x_clean[i], openpose_y_clean[i], openpose_time_clean[i]])
csv_name.close()
