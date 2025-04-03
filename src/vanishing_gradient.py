import numpy as np
import matplotlib.pyplot as plt

values = np.linspace(-10, 10, 100)

def neuron(input_):
    return 1 / (1 + np.exp(-input_))

def network(input_, depth):
    if depth == 0:
        return input_
    return neuron(network(input_, depth - 1))

plt.plot(values, network(values, 1))  # Increase depth for a deeper network
plt.show()
