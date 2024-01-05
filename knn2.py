import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class_dict = {'setosa': 0, 'versicolor': 1, 'virginica': 2}
with open('ds5.csv') as csvFile:
    dataset = [line for line in csv.reader(csvFile)]
    dataset = dataset[1:]
    X = []
    y = []
    for line in dataset:
        X.append(line[:-1])
        y.append(class_dict[line[-1]])

    X = np.array(X).astype(float)
    y = np.array(y).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

print("Accuracy: ", accuracy_score(y_test, y_pred))

print(class_dict)
print("X", "y_actual", "y_predicted", "is_correct")
for _x, _ya, _yp in zip(X_test, y_test, y_pred):
    print(_x, _ya, _yp, _ya == _yp)
