import sys
import numpy as np
import pandas as pd
import plotly
import plotly.offline as py
import plotly.graph_objects as go
import matplotlib.pyplot as plt

file = pd.read_csv(sys.argv[1])
title = '60 Hz' if 'all' in sys.argv[1] else '22 Hz'

num_points = 20 if 'all' in sys.argv[1] else 10
num_points = np.arange(1,num_points+1)

svm = [float(i[:-1]) for i in file['SVM']]
naive_bayes = [float(i[:-1]) for i in file['Naive Bayes']]
decision_tree = [float(i[:-1]) for i in file['Decision Tree']]

fig = plt.Figure()
ax = plt.axes()
ax.set_title(title)
ax.plot(num_points, svm, label='SVM')
ax.plot(num_points, naive_bayes, label='Naive Bayes')
ax.plot(num_points, decision_tree, label='Decision Tree')
ax.grid()
ax.set_xlabel('Number of points')
ax.set_ylabel('Accuracy (%)')
ax.legend()
plt.show()


# fig = go.Figure()

# fig.add_trace(go.Scatter(x=num_points, y=svm, name='SVM'))
# fig.add_trace(go.Scatter(x=num_points, y=naive_bayes, name='Naive Bayes'))
# fig.add_trace(go.Scatter(x=num_points, y=decision_tree, name='Decision Tree'))
# fig.update_layout(title=title, xaxis=dict(title="Number of points"), yaxis=dict(title="Accuracy %"))
# fig.show()


# classifiers = ['SVM', 'Naive Bayes', 'Decision Tree']
# fig = go.Figure(data=[go.Bar(name='60Hz', x=classifiers, y=[8.98, 22.02, 86.79], text=[8.98, 22.02, 86.79], textposition='auto'),
# 					go.Bar(name='22Hz', x=classifiers, y=[34.35, 29.06, 86.46], text=[34.35, 29.06, 86.46], textposition='auto')])

# fig.update_layout(barmode='group')
# fig.show()





