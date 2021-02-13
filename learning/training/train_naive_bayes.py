# Script for training with Decision Trees
import sys
import numpy as np
import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import  KFold
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

import seaborn as sn
import matplotlib.pyplot as plt

# Load the training dataset
dataset = pd.read_csv(sys.argv[1])

# Set helping variables based on the dataset (`all_frames` or `real_time`)
num_points = 20 if 'all' in sys.argv[1] else 10
dataset_path = 'all_frames' if 'all' in sys.argv[1] else 'real_time'

# Get the X, y datasets
X = dataset[dataset.columns[1:len(dataset.columns)-1]].values
y = dataset['Class'].values

# KFold splitting
n_splits = 10
kf = KFold(n_splits=n_splits, shuffle=False, random_state=None)

# Accuracy
avg_acc = [0.0 for i in range(num_points)]

# Confusion matrix
conf_matrix = [np.array([0 for i in range(25)]) for i in range(num_points)]
conf_matrix = [i.reshape(5,5) for i in conf_matrix]

# Training
for train_index, test_index in kf.split(X):
	# Training and validation datasets
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]	

	# Model object
	clf = GaussianNB()
	scores = {}

	# Training for all feature vectors and prediction on the validation dataset
	for i in range(2, len(X_train[0])+1, 2):
		clf.fit(X_train[:,:i], y_train)

		y_pred = clf.predict(X_test[:,:i])
		scores.update({i//2 : accuracy_score(y_test, y_pred)*100})
		try:
			conf_matrix[i//2-1] += confusion_matrix(y_test, y_pred)
		except:
			pass
		avg_acc[i//2-1] += scores.get(i//2)/n_splits

# Training using the training and the validation datasets and store the models
for i in range(2, len(X[0])+1, 2):
	clf = GaussianNB()
	clf.fit(X[:,:i], y)
	filename = 'models/naive_bayes/{}/{}_pixels.sav'.format(dataset_path, i//2)
	pickle.dump(clf, open(filename, 'wb'))

# Print the accuracy score
keys = [i for i in scores.keys()]
print("Accuracy metric")
print("Number of points | Accuracy")
for k in range(len(scores.keys())):
	print("{}     		 |    {}%".format(keys[k]*2,str(round(avg_acc[k],2))))

# Plot and store the confusion matrices
j=1
for matrix in conf_matrix:
	print("Number of pixels: {}".format(j))
	print(matrix)
	df_cm = pd.DataFrame(matrix, index=range(1,6), columns=range(1,6))
	
	fig = plt.figure()
	ax = plt.axes()
	ax.set_title('Confusion matrix for {} pixels'.format(j))	
	sn.heatmap(df_cm, annot=True, cmap='Blues', cbar=True)
	fig.savefig("figs/confusion_matrix/naive_bayes/{}/{}_pixels.png".format(dataset_path, j))
	j += 1
