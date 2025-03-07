import pytest
from neural import *


def test_high_logistic_function():
    assert logistic(10) > 0.9

def test_low_logistic_function():
    assert logistic(-10) < 0.1

def test_medium_logistic_function():
    assert logistic(0) == pytest.approx(0.5)

# These tests use a net with 2 input units, no hidden units, and 1 output unit.
# It eventually learns OR and AND.
# In most of the tests, the weights are initialized to specific values to test formulae.

def test_predicts_2_1():
    net = Network([2, 1])
    output = net.layers[1][0]  # The output unit
    output.weights = [-0.1, 0.1, 0.2]
    assert net.predict([0, 0])[0] == pytest.approx(0.475, abs=0.001)
    assert net.predict([0, 1])[0] == pytest.approx(0.525, abs=0.001)
    assert net.predict([1, 0])[0] == pytest.approx(0.500, abs=0.001)
    assert net.predict([1, 1])[0] == pytest.approx(0.550, abs=0.001)

def test_updates_deltas_2_1():
    net = Network([2, 1])
    output = net.layers[1][0]  # The output unit
    output.weights = [-0.1, 0.1, 0.2]
    net.predict([0, 1])
    net.reset_deltas()
    net.update_deltas([1])
    assert output.delta == pytest.approx(-0.118, abs=0.001)

def test_updates_weights_2_1():
    net = Network([2, 1])
    output = net.layers[1][0]  # The output unit
    output.weights = [-0.1, 0.1, 0.2]
    net.train([0, 1], [1])
    assert net.predict([0, 1])[0] == pytest.approx(0.583, abs=0.001)

def test_learns_or_2_1():
    net = Network([2, 1])
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    targets = [[0], [1], [1], [1]]
    for _ in range(1000):
        for i, t in zip(inputs, targets):
            net.train(i, t)
    for i, t in zip(inputs, targets):
        assert net.predict(i)[0] == pytest.approx(t[0], abs=0.2)

def test_learns_and_2_1():
    net = Network([2, 1])
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    targets = [[0], [0], [0], [1]]
    for _ in range(1000):
        for i, t in zip(inputs, targets):
            net.train(i, t)
    for i, t in zip(inputs, targets):
        assert net.predict(i)[0] == pytest.approx(t[0], abs=0.2)

# These tests use a net with 2 input units, 2 hidden units, and 1 output unit.
# It eventually learns XOR.
# In most of the tests, the weights are initialized to specific values to test formulae.

def test_predicts_2_2_1():
    net = Network([2, 2, 1])
    net.layers[2][0].weights = [-0.1, 0.1, 0.2]  # Output unit
    net.layers[1][0].weights = [-0.2, 0.3, 0.4]  # First hidden unit
    net.layers[1][1].weights = [-0.3, 0.5, -0.4]  # Second hidden unit
    assert net.predict([0, 0])[0] == pytest.approx(0.508, abs=0.001)
    assert net.predict([0, 1])[0] == pytest.approx(0.505, abs=0.001)
    assert net.predict([1, 0])[0] == pytest.approx(0.516, abs=0.001)
    assert net.predict([1, 1])[0] == pytest.approx(0.513, abs=0.001)

def test_updates_deltas_2_2_1():
    net = Network([2, 2, 1])
    net.layers[2][0].weights = [-0.1, 0.1, 0.2]  # Output unit
    net.layers[1][0].weights = [-0.2, 0.3, 0.4]  # First hidden unit
    net.layers[1][1].weights = [-0.3, 0.5, -0.4]  # Second hidden unit
    net.predict([0, 1])
    net.reset_deltas()
    net.update_deltas([1])
    assert net.layers[2][0].delta == pytest.approx(-0.124, abs=0.001)
    assert net.layers[1][0].delta == pytest.approx(-0.003, abs=0.001)
    assert net.layers[1][1].delta == pytest.approx(-0.005, abs=0.001)

def test_updates_weights_2_2_1():
    net = Network([2, 2, 1])
    net.layers[2][0].weights = [-0.1, 0.1, 0.2]  # Output unit
    net.layers[1][0].weights = [-0.2, 0.3, 0.4]  # First hidden unit
    net.layers[1][1].weights = [-0.3, 0.5, -0.4]  # Second hidden unit
    net.train([0, 1], [1])
    assert net.predict([0, 1])[0] == pytest.approx(0.549, abs=0.001)

def test_learns_xor_2_2_1():
    # NOTE: This test will occasionally fail due to a local minimum
    # If this happens, run it again.
    net = Network([2, 2, 1])
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    targets = [[0], [1], [1], [0]]
    for _ in range(1000):
        for i, t in zip(inputs, targets):
            net.train(i, t)
    for i, t in zip(inputs, targets):
        assert net.predict(i)[0] == pytest.approx(t[0], abs=0.2)

# A network with 5 hidden units is more reliable.

def test_learns_xor_2_5_1():
    net = Network([2, 5, 1])
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    targets = [[0], [1], [1], [0]]
    for _ in range(1000):
        for i, t in zip(inputs, targets):
            net.train(i, t)
    for i, t in zip(inputs, targets):
        assert net.predict(i)[0] == pytest.approx(t[0], abs=0.2)
