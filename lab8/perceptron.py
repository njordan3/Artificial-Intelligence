# Author: Nicholas Jordan
# Date: 4/7/20
# Lab 8: Perceptron Learning Algorithm Using Fisher's Iris Dataset

import csv
from random import seed
from random import random

filename = "iris.csv"

array = []

with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        row = [float(i) for i in row]
        array.append(row)

# simple 'expert system' that each sample runs through to get accuracy of the data
counter = 0
for row in array:
    if row[2] > 0 and row[4] == -1:
        counter+=1

accuracy = round(counter/len(array),2)
print("CSV species accuracy: {}%".format(accuracy*100))

# learning rate: small change to 'w' that gets made when the algorithm guesses wrong
alpha = 0.05

# seed random number generator
seed(1)

# 4 weights of random value to make guesses
#w = [random() for i in range(4)]
#theta = random()

w = [0,0,0,0]
theta = 0

# an epoch is a run through the whole dataset
for epoch in range(100):
    errors = 0
    for sample in array:
        x = sample[:4]
        yd = sample[4]

    # feed forward
        charge = x[0]*w[0] + x[1]*w[1] + x[2]*w[2] + x[3]*w[3] - theta
        #print(charge, w[0], w[1], w[2], w[3], theta)
        # sign activation function
        if charge <= 0:
            guess = -1
        else:
            guess = 1
    # error correction
        e = yd - guess
        if e != 0:
            for j in range(4):
                w[j] = w[j] + alpha * x[j] * e
            theta = theta + alpha * e * -1
            errors+=1
    print("EPOCH {}: Accuracy is {}%".format(epoch+1, round((len(array) - errors)/len(array)*100, 2)))
