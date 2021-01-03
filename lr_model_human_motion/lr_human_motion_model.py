import os

import numpy as np
import pandas as pd
import csv

from sklearn.linear_model import LinearRegression

import plotly
import plotly.graph_objects as go


csv_file = open('lr_model_all_frames.csv', 'a')
wr = csv.writer(csv_file)
row = ['FileName', 'w', 'b', 'Class']
# wr.writerow(row)

# Data
os.chdir('/home/thanasis/MSC_AI/Machine_Learning/data/csvs_clean/all_frames/MD')

with os.scandir() as entries:
	for entry in entries:
		data = pd.read_csv(entry.name)

		# Instantiate Linear Regression Model
		LR_model = LinearRegression()

		for i in range(2,len(data['x'])):
			# Fit the model
			LR_model.fit(data['x'][:i].values.reshape(-1,1), data['y'][:i])
			
			row = [entry.name, round(LR_model.coef_[0],2), round(LR_model.intercept_,2), entry.name.split('_')[1][-1]]
			wr.writerow(row)		

csv_file.close()

