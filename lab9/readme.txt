Overall Logic:
For each epoch:
    For each sample in dataset:
        feedForward()
        backpropogration() (error correction)
    output-MAD/loss()

Feedforward:
For every layer (Left to right):
    For every neuron:
        calcX()
        calcActFunct() (sigmoid)
        setY()

BackPropogation:
For every layer (Right to left):
    For every neuron:
        calc/setDelta():
            1.) output layer: delta = y * (1 - y) * (yd - y)
                                      ----------- based on activation function
            2.) "else" for all hidden layers: delta = y * (1 - y) + SUM(Wi * Deltai)
                                              delta = yH1 * (1 - yH1) * (w0,01 * delta01 + w0,02 * delta02 + ...)
        updateWeights()
        updateTheta()
