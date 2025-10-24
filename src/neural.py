import math
import random

LEARNING_RATE = 1

class Synapse:
    """
    A weighted connection from Neuron source to Neuron dest.
    """

    def __init__(self, source, dest):
        """
        :param source: The Neuron that this Synapse comes from.
        :param dest: The Neuron that this Synapse leads to.
        """
        self.source = source
        source.outputs += [self]
        self.dest = dest
        dest.inputs += [self]
        self.weight = random.gauss(0, 1)

    def weighted_output(self):
        """
        :return: The source Neuron's activation times the weight of this Synapse.
        """
        return self.weight * self.source.activation

    def update_weight(self):
        """
        Update the weight of this Synapse. Assumes source's activation and dest's delta have been set.
        """
        self.weight += -LEARNING_RATE * self.source.activation * self.dest.delta

    def feedback_delta(self):
        """
        :return: The weight of this Synapse times dest's delta.
        """
        return self.dest.delta * self.weight

class Neuron:
    """
    A unit in a neural network.
    """

    def __init__(self, previous_layer=None):
        """
        :param previous_layer: A list of Neurons in the previous layer.
        """
        self.activation = 1
        self.delta = 0
        self.inputs = []
        if previous_layer:
            Synapse(Neuron(), self)
            for n in previous_layer:
                Synapse(n, self)
        else:
            self.inputs = None
        self.outputs = []

    def __repr__(self):
        return (f'a={self.activation}, d={self.delta}, '
                f'w_i={[i.weight for i in self.inputs] if self.inputs else None}, '
                f'w_o={[o.weight for o in self.outputs] if self.outputs else None}')

    def update_activation(self):
        """
        Update the activation of this Neuron, based on its previous layer and weights.
        """
        # TODO You have to write this one
        pass  # Start by removing this line, which is just here so that the code is valid Python

    def update_delta(self, target=None):
        """
        Update the delta value for this Neuron.
        :param target: The desired output of this Neuron (if it is an output Neuron).
        """
        # TODO You have to write this one
        pass  # Start by removing this line, which is just here so that the code is valid Python

    def update_weights(self):
        """
        Update the weights of the Synapses leading into this Neuron.
        """
        # TODO You have to write this one
        pass  # Start by removing this line, which is just here so that the code is valid Python

    def set_weights(self, weights):
        """
        Sets the weights of the Synapses leading into this Neuron. Used in unit tests.
        """
        # TODO You have to write this one
        pass  # Start by removing this line, which is just here so that the code is valid Python


class Network:
    """
    A multilayer perceptron.
    """

    def __init__(self, sizes):
        """
        :param sizes: A list of the Number of neurons in each layer, e.g., [2, 2, 1] for a network that can learn XOR.
        """
        self.layers = [[]] * len(sizes)
        self.layers[0] = [Neuron() for _ in range(sizes[0])]
        for i in range(1, len(sizes)):
            self.layers[i] = [Neuron(self.layers[i-1]) for _ in range(sizes[i])]

    def predict(self, inputs):
        """
        :param inputs: Values to use as activations of the input layer.
        :return: The predictions of the neurons in the output layer.
        """
        # TODO You have to write this one
        pass  # Start by removing this line, which is just here so that the code is valid Python

    def update_deltas(self, targets):
        """
        Update the deltas of all neurons, using backpropagation. Assumes predict has already
        been called, so all neurons have had their activations updated.
        :param targets: The desired activations of the output neurons.
        """
        # TODO You have to write this one
        pass  # Start by removing this line, which is just here so that the code is valid Python

    def update_weights(self):
        """
        Update the weights of all neurons.
        """
        # TODO You have to write this one
        pass  # Start by removing this line, which is just here so that the code is valid Python

    def train(self, inputs, targets):
        """
        Feed inputs through this network, then adjust the weights so that the activations of
        the output neurons will be slightly closer to targets.
        :param inputs: A list activation values for the input units.
        :param targets: A list desired activation values for the output units.
        """
        self.predict(inputs)
        self.update_deltas(targets)
        self.update_weights()


def logistic(x):
    """
    Logistic sigmoid squashing function.
    """
    return 1 / (1 + math.exp(-x))
