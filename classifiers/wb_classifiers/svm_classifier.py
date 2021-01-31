import sys
import numpy as np
import pandas as pd

from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score


dataset = pd.read_csv(sys.argv[1])

X = dataset[dataset.columns[1:len(dataset.columns)-1]].values
y = dataset['Class'].values

kf = KFold(n_splits=20, shuffle=False, random_state=None)
avg_acc = 0.0

for train_index, test_index in kf.split(X):
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]	

	clf = SVC()
	clf.fit(X_train, y_train)

	y_pred = clf.predict(X_test)
	avg_acc += accuracy_score(y_test, y_pred)/20

print(avg_acc*100)
