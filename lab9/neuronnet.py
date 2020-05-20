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

class NeuronNetwork:
    def __init__(self, filename, membership_cols, layers, nodes_in_layer):
        self.data = self.readCSV(filename)
        self.membership_cols = membership_cols
        weight_count = len(self.data[0]) - self.membership_cols
        self.neurons = self.initializeNeurons(weight_count, layers, nodes_in_layer)
        self.layer_count = layers
        self.nodes_in_layer = nodes_in_layer

    def readCSV(self, filename):
        data = []
        with open(filename, newline='') as filename:
            csvreader = csv.reader(filename, delimiter=',')
            for row in csvreader:
                row = [float(i) for i in row]
                data.append(row)
        return data
    
    def initializeNeurons(self, weight_count, layers, nodes_in_layer):
        neurons = []
        for i in range(layers):
            row = [Perceptron(weight_count) for i in range(nodes_in_layer)]
            neurons.append(row)
        return neurons

    def startLearning(self, epochs):
        for i in range(epochs):
            for sample in self.data:
                self.feedForward(sample)
                #self.backProp(sample)

    def feedForward(self, data):
        for i in range(self.layer_count):
            for j in range(self.nodes_in_layer):
                charge = 0
                yd = []
                for k in range(len(data)):
                    if k >= len(data)-self.membership_cols:
                        yd.append(data[k])
                    else:
                        charge += data[k] * self.neurons[i][j].weight[k]
                charge -= self.neurons[i][j].theta
                # sigmoid activation function
                guess = 1 / (1 + math.exp(-charge))     
                

    def backProp(self, data):
        print("here")

Network = NeuronNetwork("iris.csv", 3, 1, 3)
Network.startLearning(1)
