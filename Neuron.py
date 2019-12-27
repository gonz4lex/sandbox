"""

Following the tutorial at https://victorzhou.com/blog/intro-to-neural-networks/.
Next steps: https://victorzhou.com/blog/intro-to-cnns-part-1/

"""



import numpy as np

# ! Define the activation function

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ! Build a Neuron class

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + bias
        return sigmoid(total)


class NeuralNet:
    
    def __init__(self,):
        weights = np.array([0, 1])
        bias = 0

        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1



def mse_loss(y, yhat):
    return ((y - yhat) ** 2).mean()

