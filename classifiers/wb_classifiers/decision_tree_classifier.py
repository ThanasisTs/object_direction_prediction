import sys
import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, confusion_matrix


dataset = pd.read_csv(sys.argv[1])

X = dataset[dataset.columns[1:len(dataset.columns)-1]].values
y = dataset['Class'].values

kf = KFold(n_splits=10, shuffle=False, random_state=None)
avg_acc = 0.0
conf_matrix = np.array([0 for i in range(25)])
conf_matrix = conf_matrix.reshape(5,5)

for train_index, test_index in kf.split(X):
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]	

	clf = DecisionTreeClassifier()
	clf.fit(X_train, y_train)
	y_pred = clf.predict(X_test)
	conf_matrix += confusion_matrix(y_test, y_pred)
	avg_acc += accuracy_score(y_test, y_pred)/10


print(avg_acc*100)
print(conf_matrix)
