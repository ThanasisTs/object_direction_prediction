# Script for testing with SVM
import os
import sys
import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sn
import matplotlib.pyplot as plt
import pickle

# Load the testing dataset
dataset = pd.read_csv(sys.argv[1])

# Set helping variables based on the dataset (`all_frames` of `real_time`)
num_points = 20 if 'all' in sys.argv[1] else 10
model_path = 'all_frames' if 'all' in sys.argv[1] else 'real_time'

# Get the X, y datasets
X = dataset[dataset.columns[1:len(dataset.columns)-1]].values
y = dataset['Class'].values

# Accuracy
acc = {}

# Confusion matrix
conf_matrix = [np.array([0 for i in range(25)]) for i in range(num_points)]
conf_matrix = [i.reshape(5,5) for i in conf_matrix]

# Store the names of the models
model_names = []
homedir = os.getcwd()
os.chdir('models/svm/{}'.format(model_path))
with os.scandir() as entries:
	for entry in entries:
		model_names.append(entry.name)
model_names = sorted(model_names)

# Prediction and store the accuracy and the confustion matrices
for i in range(2, len(X[0])+1, 2):
	clf = pickle.load(open(model_names[i//2-1], 'rb'))
	y_pred = clf.predict(X[:,:i])
	acc.update({i//2 : accuracy_score(y, y_pred)*100})
	try:
		conf_matrix[i//2-1] += confusion_matrix(y, y_pred)
	except:
		pass

# Print the accuracy score
print("Accuracy metric")
print("Number of points | Accuracy")
for k, v in acc.items():
	print("{:02d}               |    {}%".format(k, round(v,2)))

# Plot and store the confustion matrices
os.chdir(homedir)
j=1
for matrix in conf_matrix:
	df_cm = pd.DataFrame(matrix, index=range(1,6), columns=range(1,6))
	
	fig = plt.figure()
	ax = plt.axes()
	ax.set_title('Confusion matrix for {} pixels'.format(j))	
	sn.heatmap(df_cm, annot=True, cmap='Blues', cbar=True)
	fig.savefig("figs/confusion_matrix/test/svm/{}/{}_pixels.png".format(model_path, j))
	j += 1

