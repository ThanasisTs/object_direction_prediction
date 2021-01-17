import os
import numpy as np
import pandas as pd
import csv
import plotly
import plotly.graph_objects as go
import plotly.offline as py



csv_file = open('all_frames.csv', 'w')
wr = csv.writer(csv_file)

row = ['File_name']
for i in range(20):
	row.append('x'+str(i))
	row.append('y'+str(i))
row.append('Class')
wr.writerow(row)

os.chdir('/home/thanasis/MSC_AI/Machine_Learning/data/csvs_clean')

samples = {}
os.chdir('./all_frames/MD')
with os.scandir() as entries:
	for entry in entries:
		row = []
		file = pd.read_csv(entry.name)
		for i in range(len(file['x'][:20])):
			row.append(round(file['x'][i],3))
			row.append(round(file['y'][i],3))
		row.insert(0, entry.name)
		row.append(entry.name.split('_')[1][-1])
		wr.writerow(row)


os.chdir('/home/thanasis/MSC_AI/Machine_Learning/data/csvs_clean')

samples = {}
os.chdir('./all_frames/TT')
with os.scandir() as entries:
	for entry in entries:
		row = []
		file = pd.read_csv(entry.name)
		for i in range(len(file['x'][:20])):
			row.append(round(file['x'][i],3))
			row.append(round(file['y'][i],3))
		row.insert(0, entry.name)
		row.append(entry.name.split('_')[1][-1])
		wr.writerow(row)


csv_file.close()