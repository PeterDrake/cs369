# Overview
This assignment asks your team to build a working neural network from scratch.

**This is a pair assignment. When you are done, one member of your pair should submit the file, including (as a comment at the top of the file) the names of everyone who contributed.**

# Files
[`test_neural.py`](../test/test_neural.py)  
[`neural.py`](../src/neural.py)

You will be completing some classes in `neural.py`.

Note that `test_learns_xor_2_2_1` will occasionally fail (because the network gets caught in a local minimum) even if you've done everything correctly. If that happens, run it again. If it consistently fails, something is wrong.

# Optional Challenge Problems
Use inheritance, rather than copy-paste, to write HiddenNeuron.

Print out (or better yet plot) the mean squared error (between the predictions and the targets) over the course of training.

Print or plot the network's prediction for each of the four cases of the XOR problem over the course of training. On some runs, you'll see it first learn some easier function (like OR or NAND) and then have an "insight" where it figures out XOR.

For an extreme challenge, build your network using NumPy and linear algebra. It requires a different way of thinking, but the formulae become more concise and a lot of loops turn into matrix multiplication.

# What to Hand In
One member of your pair should hand in your completed version of `neural.py`. Be sure to fill in the names of everyone who contributed in the comment at the top.

*Both* of you should also fill in the [peer feedback form](https://docs.google.com/forms/d/e/1FAIpQLSe83mXCj-epu2kQ6LGW57OdCpSK5oZLgQHd7J5Nnx5MxYSsFQ/viewform?usp=sharing). If you are in a three-person team, fill it out once for each of your partners.
