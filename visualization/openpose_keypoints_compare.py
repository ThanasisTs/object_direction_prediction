import pandas as pd
import numpy as np
from scipy.spatial import distance
from scipy.stats import zscore, norm
import plotly
import plotly.offline as py
import plotly.graph_objects as go

openpose_x, openpose_y, openpose_time = {}, {}, {}
keypoints_x, keypoints_y, keypoints_time = {}, {}, {}

def read_csv(file):
    global openpose_x, openpose_y, openpose_time 
    global keypoints_x, keypoints_y, keypoints_time 
    
    fileName = pd.read_csv(file)
    file = file.split('/')[-1].split('.')[0]

    ## Keypoints
    keypoints_time[file] = [float(str(int(item[0])) + '.' + '0'*(9-len(str(int(item[1])))) + str(int(item[1]))) \
    for item in zip(fileName['/transform_topic/keypoints/0/points/header/stamp/secs'], fileName['/transform_topic/keypoints/0/points/header/stamp/nsecs']) \
            if not np.isnan(item[0])]
    keypoints_time[file] = [i-keypoints_time[file][0] for i in keypoints_time[file]]
    keypoints_x[file] = [i for i in fileName['/transform_topic/keypoints/0/points/point/x'] if not np.isnan(i)]
    keypoints_y[file] = [i for i in fileName['/transform_topic/keypoints/0/points/point/y'] if not np.isnan(i)]
    
    ## Openpose
    openpose_time[file] = [float(str(int(item[0])) + '.' + '0'*(9-len(str(int(item[1])))) + str(int(item[1]))) \
    for item in zip(fileName['/openpose_ros/human_list/header/stamp/secs'], fileName['/openpose_ros/human_list/header/stamp/nsecs']) \
            if not np.isnan(item[0])]
    openpose_time[file] = [i-openpose_time[file][0] for i in openpose_time[file]]
    openpose_x[file] = [i for i in fileName['/openpose_ros/human_list/human_list/0/body_key_points_with_prob/4/x'] if not np.isnan(i)]
    openpose_y[file] = [i for i in fileName['/openpose_ros/human_list/human_list/0/body_key_points_with_prob/4/y'] if not np.isnan(i)]


# Runs locally
read_csv("/home/thanasis/MSC_AI/Machine_Learning/data/csvs/all_frames/MD/MD_pos1_01.csv")
read_csv("/home/thanasis/MSC_AI/Machine_Learning/data/csvs/all_frames/MD/MD_pos2_01.csv")
read_csv("/home/thanasis/MSC_AI/Machine_Learning/data/csvs/all_frames/MD/MD_pos3_01.csv")
read_csv("/home/thanasis/MSC_AI/Machine_Learning/data/csvs/all_frames/MD/MD_pos4_01.csv")
read_csv("/home/thanasis/MSC_AI/Machine_Learning/data/csvs/all_frames/MD/MD_pos5_01.csv")


key_idx = list(openpose_x.keys())

stats_op, stats_points = {}, {}
for key in openpose_x.keys():
  # openpose_x[key] = zscore(openpose_x[key])
  # openpose_y[key] = zscore(openpose_y[key])
  openpose_x[key] = [(i-min(openpose_x[key]))/(max(openpose_x[key])-min(openpose_x[key])) for i in openpose_x[key]]
  openpose_y[key] = [(i-min(openpose_y[key]))/(max(openpose_y[key])-min(openpose_y[key])) for i in openpose_y[key]]
  stats_op.update({key : (np.mean(openpose_x[key]), np.std(openpose_x[key]), np.mean(openpose_y[key]), np.std(openpose_y[key]))})

for key in keypoints_x.keys():
  # keypoints_x[key] = [(i-min(keypoints_x[key]))/(max(keypoints_x[key])-min(keypoints_x[key])) for i in keypoints_x[key]]
  # keypoints_y[key] = [(i-min(keypoints_y[key]))/(max(keypoints_y[key])-min(keypoints_y[key])) for i in keypoints_y[key]]
  stats_points.update({key : (np.mean(keypoints_x[key]), np.std(keypoints_x[key]), np.mean(keypoints_y[key]), np.std(keypoints_y[key]))})

for k in stats_op.keys():
  y_op = norm.pdf(openpose_y[k], stats_op[key][2], stats_op[key][3])
  y_points = norm.pdf(keypoints_y[k], stats_points[key][2], stats_points[key][3])
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=openpose_y[k], y=y_op, mode='markers', name='Openpose'))
  fig.add_trace(go.Scatter(x=keypoints_y[k], y=y_points, mode='markers', name='Keypoints'))
  fig.update_layout(title=k)
  fig.show()



# dis_op, dis_points = {}, {}
# for key in openpose_x.keys():
#   dis = []
#   for i in range(len(openpose_x[key])):
#     dis.append(distance.euclidean([openpose_x[key][0], openpose_y[key][0]], [openpose_x[key][i], openpose_y[key][i]]))
#   dis = dis[20:]
#   print(dis)
#   zscore(dis)
#   print(dis)
#   dis_op.update({key : dis})

# for key in keypoints_x.keys():
#   dis = []
#   for i in range(len(keypoints_x[key])):
#     dis.append(distance.euclidean([keypoints_x[key][0], keypoints_y[key][0]], [keypoints_x[key][i], keypoints_y[key][i]]))
#   zscore(dis)
#   dis_points.update({key : dis})

# print("Openpose statistics")
# for motion, dis in dis_op.items():
#   print(motion, np.mean(dis), np.std(dis))

# print("Keypoints statistics")
# for motion, dis in dis_points.items():
#   print(motion, np.mean(dis), np.std(dis))


# Visualize distances
# k_op = list(dis_op.keys())[0]
# k_points = list(dis_points.keys())[0]
# fig = go.Figure(data=[go.Scatter(x=np.linspace(0, len(dis_op.get(k_op)), len(dis_op.get(k_op))), y=dis_op.get(k_op), mode='markers', name=k_op),
#                       go.Scatter(x=np.linspace(0, len(dis_points.get(k_points)), len(dis_points.get(k_points))), y=dis_points.get(k_points), mode='markers', name=k_points)],
#                 layout=go.Layout(title='Dis visualization', xaxis=dict(title='Samples(N)'), yaxis=dict(title='dis')))
# py.iplot(fig)

# Visualize Openpose pixels
fig = go.Figure(data=[go.Scatter(x=openpose_x[key_idx[i]], y=openpose_y[key_idx[i]], mode='markers', name='pos_'+str(i+1)) for i in range(5)],
               layout=go.Layout(title='Openpose pixels',
                               xaxis=dict(autorange='reversed', title='x(pixel)'),
                               yaxis=dict(title='y(pixel)')))

py.iplot(fig)

# Visualize Keypoints coordinates
fig = go.Figure(data=[go.Scatter(x=keypoints_x[key_idx[i]], y=keypoints_y[key_idx[i]], mode='markers', name='pos_'+str(i+1)) for i in range(5)],
               layout=go.Layout(title='Keypoints coordinates',
                               xaxis=dict(title='x(m)'),
                               yaxis=dict(title='y(m)')))
py.iplot(fig)