# Author: Nicholas Jordan
# Date: 4/21/20
# Lab 9: Multilayer Perceptron Neural Network

import math
import csv
from random import seed
from random import random

# seed random number generator
seed(1)

class Perceptron:
    def __init__(self, weight_count):
        self.alpha = 0.05
        self.theta = random()
        self.weight = [random() for i in range(weight_count)]

    def calcCharge(self, inputs):
        charge = 0
        for i in range(len(inputs)):
            charge += inputs[i] * self.weight[i]
        charge -= self.theta
        return charge

    def sigmoid(self, charge):
        return 1/(1+math.exp(-charge))

class NeuronNetwork:
    def __init__(self, filename):
        self.prediction_vec = []
        self.guesses = []
        self.data = self.readCSV(filename)
        self.neurons = self.initializeNeurons(4, 2, 3)

    def readCSV(self, filename):
        data = []
        with open(filename, newline='') as filename:
            csvreader = csv.reader(filename, delimiter=',')
            for row in csvreader:
                row = [float(i) for i in row]
                data.append(row)
                self.prediction_vec.append(row[-3:])
        return data
    
    def initializeNeurons(self, weight_count, layers, nodes_in_layer):
        neurons = []
        for i in range(layers):
            row = [Perceptron(weight_count) for j in range(nodes_in_layer)]
            neurons.append(row)
        return neurons

    def startLearning(self, epochs):
        for epoch in range(epochs):
            iteration = 1
            self.guesses = []
            for sample in self.data:
                guess = self.feedForward(sample[:4])
                #print("Epoch {}, Iteration {}, Prediction is {}".format(epoch+1, iteration, [round(i, 2) for i in guess]))
                self.backProp(sample)
                iteration+=1
            self.MAD(epoch)

    def feedForward(self, sample):
        #left to right
        for i in range(len(self.neurons)):
            row = []
            for j in range(len(self.neurons[0])):
                #change sample if current layer isnt first hidden layer
                if i > 0:
                    sample = []
                    for k in range(len(self.neurons[0])):
                        sample.append(self.neurons[i-1][k].y)
                charge = self.neurons[i][j].calcCharge(sample)
                self.neurons[i][j].y = self.neurons[i][j].sigmoid(charge)
                if i == len(self.neurons)-1:
                    row.append(self.neurons[i][j].y)
        self.guesses.append(row)
        return row
        
    def backProp(self, sample):
        yd = sample[-3:]
        # right to left
        for i in range(len(self.neurons)-1, -1, -1):
            for j in range(len(self.neurons[0])-1, -1, -1):
                #calc/set delta for hidden layer
                if i < len(self.neurons)-1:
                    y = self.neurons[i][j].y
                    next_layer_sum = 0
                    for k in range(len(self.neurons[0])):
                        next_layer_sum += y * self.neurons[i+1][k].delta
                    self.neurons[i][j].delta = y*(1-y)*next_layer_sum
                #calc/set delta for output layer
                else:
                    y = self.neurons[i][j].y
                    self.neurons[i][j].delta = y*(1-y)*(yd[j]-y)

                #update weights
                #if current layer isnt first hidden layer, then use last layer's outputs to adjust weights
                if i > 0:
                    for k in range(len(self.neurons[i-1])):
                        self.neurons[i][j].weight[k] += self.neurons[i][j].alpha * self.neurons[i-1][k].y * self.neurons[i][j].delta
                #else use the sample inputs from the csv to adjust the weights
                else:
                    for k in range(len(self.neurons[i][j].weight)):
                        self.neurons[i][j].weight[k] += self.neurons[i][j].alpha * sample[k] * self.neurons[i][j].delta
                self.neurons[i][j].theta += self.neurons[i][j].alpha * -1 * self.neurons[i][j].delta

    def MAD(self, epoch):
        mad_result = 0
        guess_amount = len(self.guesses)
        for i in range(guess_amount):
            for j in range(len(self.guesses[0])):
                mad_result += abs(self.prediction_vec[i][j] - self.guesses[i][j])
        print("Epoch {}, Results: MAD = {}".format(epoch+1, round(mad_result/guess_amount,5)))

Network = NeuronNetwork("iris.csv")
Network.startLearning(100)
