import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statistics import mean


def generate_coefficients():
    """
    Returns a sequence of five numbers, to be used as coefficients of a polynomial. Each number is chosen uniformly from the
    interval [-0.5, 0.5).
    """
    # TODO You have to write this


def generate_data(m, coefficients):
    """
    Returns two arrays, X and y, each of which is m by 1. The values of X are evenly spaced across the interval
    [-5.0, 5.0]. For each x, the corresponding y value is

    a + b * X + c * X**2 + d * X**3 + e * X**4 + <noise>

    where coefficients is (a, b, c, d, e) and the noise for each point is normally distributed with mean 0 and
    standard deviation 1.
    """
    # TODO You have to write this


def plot_data(X, y):
    """
    Plots X and y (as a scatter plot) and also constrains the y limit so that later, much larger values of y will not
    reset it.
    """
    plt.ylim((y.min() - 0.1 * (y.max() - y.min()),
              y.max() + 0.1 * (y.max() - y.min())))
    plt.scatter(X, y)


def generate_and_plot_data(m):
    """
    Generates m data points and plots them.
    """
    c = generate_coefficients()
    X, y = generate_data(m, c)
    plot_data(X, y)
    plt.show()


def fit_curve(X, y, degree):
    """
    Returns a trained model that fits a polynomial of the specified degree to the data.
    """
    # TODO You have to write this


def plot_curve(degree, model):
    """
    Plots a curve for model, which represents a polynomial of the specified degree.
    The x values for the curve are 100 points evenly spaced across the interval [-5.0, 5.0].
    """
    # TODO You have to write this


def mse(X, y, degree, model):
    """
    Returns the mean squared error for model (a polynomial of the specified degree) on X and y.
    """
    # TODO You have to write this


def experiment_1(m):
    """
    Generates m training points and fits models of degrees 1, 2, and 20. Plots the data and the curves for the models.
    """
    coeffs = generate_coefficients()
    X, y = generate_data(m, coeffs)
    plot_data(X, y)
    for d in [1, 2, 20]:
        model = fit_curve(X, y, d)
        plot_curve(d, model)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def experiment_2(m):
    """
    Runs the following experiment 100 times:

    Generate m training data points
    Generate 100 testing data points (using the same coefficients)
    For each d from 1 through 30, fit a curve of degree d to the training data and measure its mse on the testing data.

    After the 100 runs, plots the average mse of each degree.
    """
    mses = {i : [] for i in range(1, 31)}
    for i in range(100):
        coeffs = generate_coefficients()
        X_train, y_train = generate_data(m, coeffs)
        X_test, y_test = generate_data(100, coeffs)
        for d in range(1, 31):
            model = fit_curve(X_train, y_train, d)
            mses[d] += [mse(X_test, y_test, d, model)]
    averages = [mean(mses[d]) for d in mses]
    plt.ylim(0, 500)
    plt.plot(range(1, 31), averages)
    plt.xlabel('Degree')
    plt.ylabel('Average MSE (100 runs)')
    plt.show()


if __name__ == '__main__':
    # generate_and_plot_data(100)
    # experiment_1(20)
    # experiment_2(20)
    pass
