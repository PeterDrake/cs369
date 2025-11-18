# Overview
For this challenging final project, your team will build a neural network to identify buildings as part of an [environmental study](data_description.docx). Given the canvas height map, your network should output an array of the same size where each pixel has a value between 0.0 (definitely not a building) and 1.0 (definitely a building).

Your main task is to define the neural network. It should have an input size of `(1000, 1000, 1)`. The output should be the same size.

**This is a team assignment. When you are done, one member of your team should submit the file, including (as a comment at the top of the file) the names of everyone who contributed.**

# Sparse Data
One complication in this task is that almost all pixels in the training data are *not* buildings. The network can get very good accuracy (around 98%) by declaring that *nothing* is a building (always outputting 0).

To get around this, we're using the `weighted_cross_entropy_with_logits` loss function. This provides a larger penalty for false negatives (missing a builiding) than false positives (saying something is a building when it's not). You should therefore pay more attention to *loss* than to *accuracy*.

# Files
* [`BatchGenerator.py`](../../cs369_solutions/src/BatchGenerator.py) This is used to gather the data into batches for training the network.
* [`lidar_net.py`](../../cs369_solutions/src/lidar_net.py) This is an incomplete skeleton of the program to build and train the network. You'll have to supply the network definition.
* [`lidar_net.sh`](../../cs369_solutions/src/lidar_net.py) This is the script to run `lidar_net.py` on BLT.

# Hints
* You can run your network on BLT. ***Start early!*** Other people in the class will also be running jobs on BLT, especially as the deadline approaches.
* Since this assignment is due on the last day of classes, ***there is no grace period for this assignment***. Hand in *something* on time!
* This is going to take a lot of trial and error. Start early and be prepared to launch a run and get some other work done while you wait for it to finish.
* BLT too busy? Try running without using GPUs. I *think* it will take longer, but you'll still be making progress. You might even be able to run your network on your own machine.
* Start by connecting a single Conv2D layer directly to the inputs to make sure everything runs and establish a baseline. Then try to improve on it.

# Optional Challenge Problems
* Do better than I did! (Specifically, get a final validation loss less than 1.2876.)
* Save (and hand in) some pictures to compare the correct answers to the network predictions.
* Plot (and hand in) the learning curve.
* Figure out how to save (and reload) the trained model.
* Explore! Try different network architectures and play with other hyperparameters

# What to Hand in
One member of your team should hand in:
* Your completed version of `lidar_net.py`.
* The output of running your program.

Be sure to fill in the names of everyone who contributed in the comment at the top.