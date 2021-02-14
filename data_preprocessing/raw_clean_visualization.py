import os
import sys
import numpy as np
import pandas as pd
import plotly
import plotly.offline as py
import plotly.graph_objects as go


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

x, y, time = {}, {}, {}
print("Give 'filter' as arg to visualize the filtered data, otherwist pass nothing")
read_csv('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs/all_frames/TT/TT_pos1_01.csv')
read_csv('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs/all_frames/TT/TT_pos2_01.csv')
read_csv('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs/all_frames/TT/TT_pos3_01.csv')
read_csv('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs/all_frames/TT/TT_pos4_01.csv')
read_csv('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs/all_frames/TT/TT_pos5_01.csv')


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
fig_raw = go.Figure(data=[go.Scatter(x=x[key_idx[i]], y=y[key_idx[i]], mode='markers', marker=dict(color=c[key_idx[i]]), showlegend=False)  for i in range(len(key_idx))],
               layout=go.Layout(title='Raw Openpose pixels',
                               xaxis=dict(title='x(pixel)'),
                               yaxis=dict(autorange='reversed', title='y(pixel)')))

fig_raw.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='red'), name='pos1'))
fig_raw.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='green'), name='pos2'))
fig_raw.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='blue'), name='pos3'))
fig_raw.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='yellow'), name='pos4'))
fig_raw.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='orange'), name='pos5'))
fig_raw.update_layout(showlegend=True)

py.iplot(fig_raw)

x, y, time = {}, {}, {}
read_clean_csv('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs_clean/all_frames/TT/TT_pos1_01.csv')
read_clean_csv('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs_clean/all_frames/TT/TT_pos2_01.csv')
read_clean_csv('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs_clean/all_frames/TT/TT_pos3_01.csv')
read_clean_csv('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs_clean/all_frames/TT/TT_pos4_01.csv')
read_clean_csv('/home/thanasis/MSC_AI/Machine_Learning/ML/data/csvs_clean/all_frames/TT/TT_pos5_01.csv')

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
fig_clean = go.Figure(data=[go.Scatter(x=x[key_idx[i]], y=y[key_idx[i]], mode='markers', marker=dict(color=c[key_idx[i]]), showlegend=False)  for i in range(len(key_idx))],
               layout=go.Layout(title='Clean Openpose pixels',
                               xaxis=dict(title='x(pixel)'),
                               yaxis=dict(autorange='reversed', title='y(pixel)')))

fig_clean.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='red'), name='pos1'))
fig_clean.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='green'), name='pos2'))
fig_clean.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='blue'), name='pos3'))
fig_clean.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='yellow'), name='pos4'))
fig_clean.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='orange'), name='pos5'))
fig_clean.update_layout(showlegend=True)

py.iplot(fig_clean)
