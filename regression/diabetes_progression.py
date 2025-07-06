import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, model_selection # Here model_selection is used for splitting data into training and test sets

# Loading the diabetes dataset.
# return_X_y signals that X will be the data matrix and y will be the regression target.
# What you are getting back in a response is a tuple
X, y = datasets.load_diabetes(return_X_y=True)

# Analyze and preprossing the data.
print(X.shape)
print(X[0])
X = X[:, 2] # select 3rd column of the data matrix
X = X.reshape((-1, 1)) # reshape to a 2D array with one column
print(X.shape)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33)

# Creating and training the model 
# Create a linear regression model and fit it to the training data.
model = linear_model.LinearRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)
print(X_test[:5])
print(y_pred[:5])

# Plotting the results
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Scaled BMI')
plt.ylabel('Disease Progression')
plt.title('A Graph Plot Showing Diabetes Progression Against BMI')
plt.show()