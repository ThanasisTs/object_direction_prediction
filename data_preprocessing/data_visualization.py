import os
import sys
import numpy as np
import pandas as pd
import plotly
import plotly.offline as py
import plotly.graph_objects as go

x, y, time = {}, {}, {}

def read_csv(file):
    global x, y, time 
    
    fileName = pd.read_csv(file)
    file = file.split('/')[-1].split('.')[0]

    ## Openpose
    time[file] = [float(str(int(item[0])) + '.' + '0'*(9-len(str(int(item[1])))) + str(int(item[1]))) \
    for item in zip(fileName['/openpose_ros/human_list/header/stamp/secs'], fileName['/openpose_ros/human_list/header/stamp/nsecs']) \
            if not np.isnan(item[0])]
    time[file] = [i-time[file][0] for i in time[file]]
    x[file] = [i for i in fileName['/openpose_ros/human_list/human_list/0/body_key_points_with_prob/4/x'] if not np.isnan(i)]
    y[file] = [i for i in fileName['/openpose_ros/human_list/human_list/0/body_key_points_with_prob/4/y'] if not np.isnan(i)]

def read_clean_csv(file):
    global x, y, time 
    
    fileName = pd.read_csv(file)
    file = file.split('/')[-1].split('.')[0]

    ## Openpose
    x[file] = fileName['x']
    y[file] = fileName['y']

# Runs locally

print("Give 'filter' as arg to visualize the filtered data, otherwist pass nothing")
try:
    if sys.argv[1] == 'filter':
        os.chdir('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs_clean/all_frames/TT') 
        with os.scandir() as entries:
        	for entry in entries:
        		read_clean_csv(entry.name)
except:
    os.chdir('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs/all_frames/TT')
    with os.scandir() as entries:
        for entry in entries:
            read_csv(entry.name)

key_idx = list(x.keys())
c = {}
for key in key_idx:
	if 'pos1' in key:
		c[key] = 'red'
	elif 'pos2' in key:
		c[key] = 'green'
	elif 'pos3' in key:
		c[key] = 'blue'
	elif 'pos4' in key:
		c[key] = 'yellow'
	else:
		c[key] = 'orange'
	

# Visualize Openpose pixels
fig = go.Figure(data=[go.Scatter(x=x[key_idx[i]], y=y[key_idx[i]], mode='markers', marker=dict(color=c[key_idx[i]]), showlegend=False)  for i in range(len(key_idx))],
               layout=go.Layout(title='Openpose pixels',
                               xaxis=dict(autorange='reversed', title='x(pixel)'),
                               yaxis=dict(title='y(pixel)')))

fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='red'), name='pos1'))
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='green'), name='pos2'))
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='blue'), name='pos3'))
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='yellow'), name='pos4'))
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='orange'), name='pos5'))
fig.update_layout(showlegend=True)

py.iplot(fig)