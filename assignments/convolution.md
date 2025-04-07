# Overview

This assignment gives you practice building a convolutional neural network for a computer vision task (handwriting recognition). Specifically, you are building a network to perform the MNIST classification task (not to be confused with Fashion MNIST).

Big advantages of neural networks include (a) reducing the number of weights when processing large images and (b) providing translation invariance so it doesn't matter exactly where in the image an object appears. Since the MNIST data are small, and already cropped and centered, this may be overkill. I wanted you to have practice on an easy problem before applying convolutional neural network to more challenging data in the next assignment.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Files
[conv_mnist.py](../src/conv_mnist.py)

You will modify this file to replace the dense network with a convolutional one.

# Hints
You need to specify that the input shape is `[28, 28, 1]`. (The 1 is because these grayscale images have one channel per pixel, whereas color images have 3.)

Add a flattening layer *after* the convolutional layers, not before.

I used three convolutional layers, each with kernel size 3, ReLU activation, and He initialization. They had 32, 64, and 128 filters, respectively.

30 epochs was too long to train my convolutional network; 5 was plenty.

You are welcome, but not required, to make use of BLT for this assignment.

# Optional Challenge Problems
Play with the network architecture or other hyperparameters. Can you either improve the performance of the network or get the same performance with a simpler network?

Determine the number of parameters in the dense network and your convolutional network.

Use early stopping to stop training when validation performance starts to get worse.

For a major challenge, try tackling the [Cat vs Dog Dataset on kaggle](https://www.kaggle.com/datasets/karakaggle/kaggle-cat-vs-dog-dataset).

# What to Hand in
Hand in your updated version of `conv_mnist.py` and the output of running it. Don't forget to uncomment the line that tests the final network, but only after you've stopped making changes.
