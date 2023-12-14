# -*- coding: utf-8 -*-
"""MLPROJECT_WASIULLAH.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZlQozakhzzkmlrEBytu8aRhqHUngMW50
"""

#importing the necessary libraries
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import train_test_split

#reading dataset
my_data = pd.read_csv("heart.csv")

my_data.head()

#feature column names
feature_columns = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']

#changing string values to text
my_data = my_data.apply(LabelEncoder().fit_transform)

X_1 = my_data[feature_columns] # Features\n",
y_1 = my_data.HeartDisease # Target variable\n"

#taking mean and standard deviation of data for scaling
X_1 -= np.mean(X_1, axis=0)
X_1 /= np.std(X_1, axis=0)

#splitting data into train, validation and test datasets
X_train1, X_test, y_train1, y_test = train_test_split(X_1, y_1, test_size=0.2, random_state=0)
X_train, X_val, y_train, y_val = train_test_split(X_train1, y_train1, test_size=0.2, random_state=0)

#setting initializing values of parameter and lambda
lamda = 1000
Params = [25, 46, 24, 20, 47, 31, 36, 29, 39, 27, 34, 23]

#sigmoid function for hypothesis
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

#hypothesis function
def hypothesis(training_data, P):
  a = []
  for index, row in training_data.iterrows():
    g = P[0] + (P[1] * row[0]) + (P[2] * row[1]) + (P[3] * row[2]) + (P[4] * row[3]) + (P[5] * row[4]) + (P[6] * row[5]) + (P[7] * row[6]) + (P[8] * row[7]) + (P[9] * row[8]) + (P[10] * row[9]) + (P[11] * row[10])
    a = a + [sigmoid(g)] #calling sigmoid function
  return a

def regularization(P, X_traini):
  squared = [number ** 2 for number in P]
  squared_P = np.sum(squared)
  div = 2 * len(X_traini)
  reg = (lamda/div) * squared_P
  return reg

def cost(weights, train_data, labels_data):
  model_data = hypothesis(train_data, weights)
  dad = np.subtract(1,model_data)
  dadd = dad + 0.000001
  daddd = np.log(dadd)
  JJ = np.sum(np.multiply(labels_data,np.log(model_data)) + np.multiply((np.subtract(1,labels_data)),daddd))
  JJ_1 = -JJ/len(train_data)
  JJJ_1 = JJ_1 + regularization(weights, train_data)
  return JJJ_1

def reularization_descent(X_traini,Params):
    lamda = 10000
    divi = lamda/len(X_traini)
    divident = round(divi)
    calc = [value * divident for value in Params]
    return calc

#calculating the values of gradients
def calc_gradients(Params, L, X_traini, labels):
  g = np.zeros(12)
  hypos = hypothesis(X_traini, Params)
  reg = np.array(reularization_descent(X_traini,Params))
  d = np.subtract(hypos,labels)
  g[0] = -1 * (np.sum(np.subtract(hypos,labels)))
  g[1] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,0]))) + (reg[1]))
  g[2] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,1]))) + (reg[2]))
  g[3] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,2]))) + (reg[3]))
  g[4] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,3]))) + (reg[4]))
  g[5] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,4]))) + (reg[5]))
  g[6] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,5]))) + (reg[6]))
  g[7] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,6]))) + (reg[7]))
  g[8] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,7]))) + (reg[8]))
  g[9] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,8]))) + (reg[9]))
  g[10] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,9]))) + (reg[10]))
  g[11] = -1 * ((np.sum(np.multiply(d,X_traini.iloc[:,10]))) + (reg[11]))
  g_1 = g/len(X_traini)
  return g_1

#implementation of gradient descent algorithm
def descent(w_new, P, lr, X_train, y_train):
    print(P)
    print(cost(P, X_train, y_train))
    hypo = hypothesis(X_train, P)
    j=0
    J = [] #list to calculate the errors
    no_of_iters = 2000
    # runs for number for desired iterations
    for epoch in range(no_of_iters):
        P = w_new
        w0 = P[0] + lr*calc_gradients(P, hypo, X_train, y_train)[0]
        w1 = P[1] + lr*calc_gradients(P, hypo, X_train, y_train)[1]
        w2 = P[2] + lr*calc_gradients(P, hypo, X_train, y_train)[2]
        w3 = P[3] + lr*calc_gradients(P, hypo, X_train, y_train)[3]
        w4 = P[4] + lr*calc_gradients(P, hypo, X_train, y_train)[4]
        w5 = P[5] + lr*calc_gradients(P, hypo, X_train, y_train)[5]
        w6 = P[6] + lr*calc_gradients(P, hypo, X_train, y_train)[6]
        w7 = P[7] + lr*calc_gradients(P, hypo, X_train, y_train)[7]
        w8 = P[8] + lr*calc_gradients(P, hypo, X_train, y_train)[8]
        w9 = P[9] + lr*calc_gradients(P, hypo, X_train, y_train)[9]
        w10 = P[10] + lr*calc_gradients(P, hypo, X_train, y_train)[10]
        w11 = P[11] + lr*calc_gradients(P, hypo, X_train, y_train)[11]
        #updating the values of all parameters into w_new
        w_new = [w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11]
        print(w_new)
        print(cost(w_new, X_train, y_train))

        J = J + [cost(w_new, X_train, y_train)]
    return w_new, J

w, loss = descent(Params,Params,0.1, X_train, y_train)

#plot for Learning curves for logistic regression model
epochs = [x for x in range(2000)]
plt.style.use('seaborn')
plt.plot(epochs, loss, label = 'Training error')
#plt.plot(epochs, loss, label = 'Validation error')
plt.ylabel('Error', fontsize = 14)
plt.xlabel('No of Epochs', fontsize = 14)
plt.title('Learning curves for logistic regression model', fontsize = 18, y = 1.03)
plt.legend()

def predictions(new_P, test_data):
  b = []
  for index, row in test_data.iterrows():
    z = new_P[0] + (new_P[1] * row[0]) + (new_P[2] * row[1]) + (new_P[3] * row[2]) + (new_P[4] * row[3]) + (new_P[5] * row[4]) + (new_P[6] * row[5]) + (new_P[7] * row[6]) + (new_P[8] * row[7]) + (new_P[9] * row[8]) + (new_P[10] * row[9]) + (new_P[11] * row[10])
    m = 1/(1 + np.exp(-z))
    b = b + [m]
  return b

a = predictions(w, X_val)
b = predictions(w, X_test)
c = predictions(w, X_train)

D = [round(a) for a in a]
E = [round(b) for b in b]
F = [round(c) for c in c]

print('Accuracy Score on training data: ', accuracy_score(y_train,F))

print('Accuracy Score on validation data: ', accuracy_score(y_val,D))

print('Accuracy Score on test data: ', accuracy_score(y_test,E))

print(classification_report(y_val,D))

print(classification_report(y_test,E))

precision, recall, thresholds = precision_recall_curve(y_val,D)