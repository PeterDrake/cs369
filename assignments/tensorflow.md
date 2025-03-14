# Overview

This assignment has you using TensorFlow to build a neural network to recognize handwritten digits.

This is, in some sense, a "cut and paste" job; you won't be writing much code. It is meant to give you practice:
* determining which code to cut and paste, which means reading Géron's Colab notebook fairly closely,
* making (very) slight modifications to the code, and
* dealing with the inevitable complications that arise.

The task is simple: train a network to classify the digits in the MNIST dataset.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Hints
Start with Géron's [notebook for chapter 10](https://github.com/ageron/handson-ml3/blob/main/10_neural_nets_with_keras.ipynb). Copy the necessary code (and no more) into a file called `mnist.py`. Modify it to use the `mnist` dataset instead of `mnist_fashion`.

Your program should train the network and show the final training and validation accuracy. If you use exactly the same settings as in the `mnist_fashion` example, the validation accuracy should be around 98%.

On a Mac, if you get a `ssl.SSLCertVerificationError` when trying to load the data, try running this once from the command line (adapting the Python version to whatever you have installed):
```
/Applications/Python\ 3.13/Install\ Certificates.command
```

# Optional Advanced Problems
Tune the hyperparameters of the network. Can you either get better validation performance or get the same performance with a smaller network?

# What to Hand in
Hand in your completed version of `mnist.py`.