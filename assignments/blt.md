# Overview

This assignment is to meant to give you practice using the BLT high-performance computing cluster before building more challenging neural networks. *In theory* it should be easy, but I expect many people will run into complications.

The task is to build a network to predict customer satisfaction with sub sandwiches based on a number of factors including food appearance, menu variety, and restaurant decor.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Files
[`sandwich.py`]('../src/sandwich.py')

You will also need to download `Sub_Sandwiches_OSAT.csv` from [kaggle](https://www.kaggle.com/datasets/kane6543/sub-sandwich-customer-satisfaction-score). This will require you to make an account, but you don't have to use your real name and you can delete it after the course is over.

# Steps
1. Read the description of the dataset on kaggle so you understand the features.
2. Read through `sandwich.py`. Make sure you understand what each step does and why we're doing it.
3. Run `sandwich.py` on a local machine. When I did this, I got a final accuracy of 0.3712 on the test set. This is not great, but it's considerably better than the "chance" accuracy of $1/7 \approx 0.1429$.
4. Create a shell script `sandwich.sh` similar to the one provided in [Jeremy's notes on BLT](http://bit.ly/cs369-blt).
5. Use `sftp` to transfer all three files up to BLT.
6. On BLT:
   1. Activate the virtual environment.
   2. Use SLURM to launch `sandwich.sh`.
   3. Wait for the program to finish. You can use the `squeue` command to see what's still running. If you're successfully using the GPUs, your program should run briefly on the `sprouts` node.
   4. Examine the output file. There will be some warnings at the beginning, but if everything worked right it should run to completion.
7. Use `sftp` to retrieve your output file

# Optional Challenge Problems
Find a way to get better accuracy by messing with hyperparameters like the number of layers and neurons per layer in the network.

Get the same accuracy with a smaller, simpler, less computationally-intensive network.

Get the network to overfit the data. Explain how you know that overfitting is occurring.

Cast this as a regression task. It's debatable whether this is a classification or regression task. MNIST and Fashion MNIST are clearly classification tasks -- if the network guesses the wrong category, it's wrong. Here, if the correct output was 6, an output of 1 seems more wrong than 5. On the other hand, these aren't numbers on a ratio scale like prices or weights; the difference between 5 and 6 may not be the same size as the difference between 3 and 4. To make this a regression task, scale the correct outputs into the range [0, 1]. Train a network with a single sigmoid output unit. It should produce something close to 1 for sandwiches where customers had maximum overall satisfaction (7 in the original data) and something close to 0 when they had minimum overall satisfaction (1).

Try linear regression. Does it do as well as the network? In other words, is a neural network overkill for this task?

Explore kaggle more deeply, tackling some of their other challenges. This is a particularly good investment of time if you're a data science minor.

# What to Hand in
Hand in the output file generated on BLT.

If you did any challenge problems, hand in any relevant files (like alternate versions of `sandwich.py`) and explain what you did.
