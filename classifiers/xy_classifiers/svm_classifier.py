import sys
import numpy as np
import pandas as pd

from sklearn.svm import SVC
from sklearn.model_selection import  KFold
from sklearn.metrics import accuracy_score


dataset = pd.read_csv(sys.argv[1])

X = dataset[dataset.columns[1:len(dataset.columns)-1]].values
y = dataset['Class'].values

kf = KFold(n_splits=20, shuffle=False, random_state=None)
avg_acc = [0.0 for i in range(20)]

for train_index, test_index in kf.split(X):
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]	

	clf = SVC()
	scores = {}
	for i in range(2, len(X_train[0])+1, 2):
		clf.fit(X_train[:,:i], y_train)

		y_pred = clf.predict(X_test[:,:i])
		scores.update({i//2 : accuracy_score(y_test, y_pred)*100})
		avg_acc[i//2] += scores.get(i//2)/20

keys = [i for i in scores.keys()]
for k in range(len(scores.keys())):
	print(keys[k],str(round(avg_acc[k],2))+'%')

