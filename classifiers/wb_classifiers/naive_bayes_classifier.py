import sys
import numpy as np
import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


dataset = pd.read_csv(sys.argv[1])

X = dataset[dataset.columns[1:len(dataset.columns)-1]]
y = dataset['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)

nb = GaussianNB()
nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)
print(accuracy_score(y_test, y_pred)*100)
