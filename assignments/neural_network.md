# Overview
This assignment asks your team to build a working neural network from scratch.

**This is a team assignment. When you are done, one member of your team should submit the file, including (as a comment at the top of the file) the names of everyone who contributed.**

# Files
[`test_neural.py`](../test/test_neural.py)  
[`neural.py`](../src/neural.py)

You will be completing some classes in `neural.py`.

Note that `test_learns_xor_2_2_1` will occasionally fail (because the network gets caught in a local minimum) even if you've done everything correctly. If that happens, run it again. If it consistently fails, something is wrong.

# Hints
You will probably spend a lot of time debugging this one. You may find it useful to write `__str__` methods. I've provided one for `Synapse`, but not for `Neuron`. You may also find it helpful to write additional unit tests (in a separate test file -- don't modify the existing one) that test whatever behavior isn't working.

# Optional Challenge Problems
Print out (or better yet plot) the mean squared error (between the predictions and the targets) over the course of training.

Print or plot the network's prediction for each of the four cases of the XOR problem over the course of training. On some runs, you'll see it first learn some easier function (like OR or NAND) and then have an "insight" where it figures out XOR.

For an extreme challenge, build your network using NumPy and linear algebra. It requires a different way of thinking, but the formulae become more concise and a lot of loops turn into matrix multiplication.

# What to Hand In
One member of your team should hand in your completed version of `neural.py`. Be sure to fill in the names of everyone who contributed in the comment at the top.
