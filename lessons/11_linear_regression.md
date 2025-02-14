Attendance
Ripped From Today's Headlines

# Linear Regression
* Idea: predict a number y from a number x
  * Example in the book: predict life satisfaction from GDP per capita
  * The family of models here are lines
  * The parameters are the slope and intercept of the line
  * There is some line that best fits the data
* Let's generate some data
```python
import random

random.seed(0)

n = 3  # Number of data points

theta = [0.1, 0.2]  # Parameters of the true model

xs = [random.random() for _ in range(n)]
ys = [theta[0] + theta[1] * x for x in xs]

print(xs, ys)
```

* Let's plot them
```python
import matplotlib.pyplot as plt

...

plt.plot(xs, ys, 'b.')
plt.show()
```
* Try 100 data points
* Add noise:
```python
ys = [theta[0] + theta[1] * x + random.gauss(0, 0.02) for x in xs]
```
* Plot the actual line through the data
```python
x_model = [0, 1]
y_model = [theta[0] + theta[1] * x for x in x_model]

...

plt.plot(x_model, y_model, 'r')
```
* Of course, with real data, we don't know the actual source of the data
  * We can find the line that minimizes RMSE (or equivalently, MSE)
  * Plan A: trial and error
  * Plan B: a closed form solution exists
    * How is it derived? Ask Yung-Pin
    * There is not such a solution for some more complicated models
  * Plan C: gradient descent

[The book's code](https://github.com/ageron/handson-ml3/blob/main/04_training_linear_models.ipynb)

* If extra time, work on assignments

# For Next Time
You can now start work on linear regression assignment  
Read Chapter 3
