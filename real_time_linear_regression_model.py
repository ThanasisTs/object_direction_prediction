import sys

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

import plotly
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# use raw_data_clean.csv file for demonstration
# Data
data = pd.read_csv(sys.argv[1])

# Instantiate Linear Regression Model
LR_model = LinearRegression()

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
		html.H1("Real-Time Update of LR Model", style={'text-align' : 'center'}),

		html.Button("Time step", id='increase_time_step', n_clicks=1),
		html.Div(id='container-button', children=[]),

		dcc.Graph(id='LR_fig', figure={})
	])

# Define app callaback
@app.callback(
		[Output(component_id='container-button', component_property='children'),
		Output(component_id='LR_fig', component_property='figure')],
		[Input(component_id='increase_time_step', component_property='n_clicks')]
)

# App callback
def update_graph(n_points):

	# Fit the model
	LR_model.fit(data['x'][:n_points].values.reshape(-1,1), data['y'][:n_points])
	
	# Train results
	w = LR_model.coef_
	b = LR_model.intercept_
	train_res = w*np.array(data['x']) + b

	# Visualize the training data and the fitted linear model
	container = "w={}, b={}".format(round(w[0],4),round(b,2))
	fig = go.Figure(data=[go.Scatter(x=data['x'], y=data['y'], mode='markers', name='Whole data'),
						go.Scatter(x=data['x'][:n_points], y=data['y'][:n_points], mode='markers', name='Current data'),
						go.Scatter(x=data['x'][:n_points], y=train_res, mode='lines', name='Linear Model')],
	               layout=go.Layout(title='Update of linear model',
	                               xaxis=dict(autorange='reversed', title='x(pixel)'),
	                               yaxis=dict(title='y(pixel)')))


	return container, fig


if __name__ == "__main__":
	app.run_server(debug=True)
