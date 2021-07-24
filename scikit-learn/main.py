#%% 1.1 Linear Model
# regression: opposite of progression
from sklearn import linear_model
regression = linear_model.LinearRegression()
regression.fit([[0, 0], [1, 1], [2, 2], [3, 3]], [0, 1, 2, 2], sample_weight=None)
regression.coef_

# %%
import matplotlib.pyplot as plt
x = [i for i in range(10)]
y = [2*i for i in range(10)]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel("y-axis")
plt.scatter(x,y)


# %%

# %%
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
iris = datasets.load_iris()
X = iris.data
y = iris.target
""" 
print(X.shape)
print(y.shape) """

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 
# test_size is the percentage of the dataset for validing the training Dataset
# .shape is the size of the dataset for each job
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# %%
import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("car.data")
""" print(data.head()) """

# X are the labels
# .values shows in Matrix form(string)
X = data[['buying', 'maint', 'safety']].values

y = data[['class']]
print(X,y)


# CONVERSION1 this is for converting the string label into number so the ML can work on
labelencoder = LabelEncoder()
for i in range(len(X[0])):
    X[:,i] = labelencoder.fit_transform(X[:, i])
# 3 is vhigh, 2 is high etc....

# CONVERSION2 this method has a rule
label_mapping = {
    'unacc':0,
    'acc':1,
    'good':2,
    'vgood':3
}
y['class'] = y['class'].map(label_mapping)
print(X)
y = np.array(y) # conversion into numpy array
print(y)
# %%
