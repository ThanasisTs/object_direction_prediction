import sys
import numpy as np
import pandas as pd

from sklearn.svm import SVC
from sklearn.model_selection import  KFold
from sklearn.metrics import accuracy_score, confusion_matrix


dataset = pd.read_csv(sys.argv[1])

X = dataset[dataset.columns[1:len(dataset.columns)-1]].values
y = dataset['Class'].values

kf = KFold(n_splits=10, shuffle=False, random_state=None)
avg_acc = [0.0 for i in range(10)]
conf_matrix = [np.array([0 for i in range(25)]) for i in range(10)]
conf_matrix = [i.reshape(5,5) for i in conf_matrix]

for train_index, test_index in kf.split(X):
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]	

	clf = SVC()
	scores = {}
	for i in range(2, len(X_train[0])+1, 2):
		clf.fit(X_train[:,:i], y_train)

		y_pred = clf.predict(X_test[:,:i])
		scores.update({i//2 : accuracy_score(y_test, y_pred)*100})
		try:
			conf_matrix[i//2-1] += confusion_matrix(y_test, y_pred)
		except:
			pass
		avg_acc[i//2-1] += scores.get(i//2)/10

keys = [i for i in scores.keys()]
for k in range(len(scores.keys())):
	print(keys[k],str(round(avg_acc[k],2))+'%')

j=2
for i in conf_matrix:
	print("Number of pixels: {}".format(j))
	print(i)
	j += 2
