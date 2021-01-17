import os
import numpy as np
import pandas as pd

import plotly
import plotly.graph_objects as go
import plotly.offline as py

os.chdir('/home/thanasis/MSC_AI/Machine_Learning/data/csvs_clean')
homedir = os.getcwd()

samples = {}
os.chdir('./real_time/MD')
with os.scandir() as entries:
	for entry in entries:
		file = pd.read_csv(entry.name)
		samples[entry.name] = len(file['x'])

os.chdir('../TT')
with os.scandir() as entries:
	for entry in entries:
		file = pd.read_csv(entry.name)
		samples[entry.name] = len(file['x'])

print(samples.values())
fig = go.Figure(data=[go.Scatter(x=np.linspace(0, len(samples), len(samples)), y=list(samples.values()), mode='markers')],
				layout=go.Layout(title="Number of examples", xaxis=dict(title='Samples(N)'), yaxis=dict(title='Examples(M)')))

py.iplot(fig)


print(list(samples.keys())[list(samples.values()).index(min(list(samples.values())))])
print(list(samples.keys())[list(samples.values()).index(max(list(samples.values())))])
