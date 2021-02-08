import sys
import numpy as np
import pandas as pd

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix

dataset = pd.read_csv(sys.argv[1])
num_points = 20 if 'all' in sys.argv[1] else 10
n_splits = 10

X = dataset[dataset.columns[1:len(dataset.columns)-1]].values
y = dataset['Class'].values


kf = KFold(n_splits=n_splits, shuffle=False, random_state=None)
avg_acc = [0.0 for i in range(num_points)]
conf_matrix = [np.array([0 for i in range(25)]) for i in range(num_points)]
conf_matrix = [i.reshape(5,5) for i in conf_matrix]

parameters = {'kernel' : ('linear', 'rbf'), 'C' : [1, 10]}

for train_index, test_index in kf.split(X):
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]	
	# st_x = StandardScaler()
	# st_y = StandardScaler()

	# X = st_x.fit_transform(X)
	# y = st_y.fit_transform(y.reshape(-1,1))

	# clf = SVC()
	svc = SVC()
	clf = GridSearchCV(svc, parameters)
	scores = {}
	
	for i in range(2, len(X_train[0])+1, 2):
		clf.fit(X_train[:,:i], y_train)

		y_pred = clf.predict(X_test[:,:i])
		scores.update({i//2 : accuracy_score(y_test, y_pred)*100})
		try:
			conf_matrix[i//2-1] += confusion_matrix(y_test, y_pred)
		except:
			pass
		avg_acc[i//2-1] += scores.get(i//2)/n_splits

keys = [i for i in scores.keys()]
print("Accuracy metric")
print("Number of points | Accuracy")
for k in range(len(scores.keys())):
	print("{}     		 |    {}%".format(keys[k]*2,str(round(avg_acc[k],2))))

# j=2
# for i in conf_matrix:
# 	print("Number of pixels: {}".format(j))
# 	print(i)
# 	j += 2
