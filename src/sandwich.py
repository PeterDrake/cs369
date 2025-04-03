import numpy as np
import pandas as pd
import tensorflow as tf

# Set the random seeds
np.random.seed(0)
tf.random.set_seed(0)

# Read the data file
data = pd.read_csv('../Sub_Sandwiches_OSAT.csv')

# Discard a couple of columns that we won't be using
data.pop('Respondent_Serial')  # Not be meaningful for new data
data.pop('brand')  # Categorical

# Discard any rows containing missing values
data.dropna(how='any', inplace=True)

# Shuffle the data for good measures
data = data.sample(frac=1)  # See https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows

# Extract the correct answers
labels = data.pop('OSAT') - 1  # The -1 is so that the labels are 0-6 instead of 1-7

# Extract training, validation, and test sets
n = len(data)
train_end = n * 6 // 10
valid_end = n * 8 // 10
X_train, y_train = data[:train_end], labels[:train_end]
X_valid, y_valid = data[train_end:valid_end], labels[train_end:valid_end]
X_test, y_test = data[valid_end:], labels[valid_end:]

# Define the network
model = tf.keras.Sequential([
    tf.keras.layers.Input([40]),
    tf.keras.layers.Dense(300, activation="relu"),
    tf.keras.layers.Dense(100, activation="relu"),
    tf.keras.layers.Dense(7, activation="softmax")
])

# Compile the network
model.compile(loss="sparse_categorical_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])

# Train the network
# Note: verbose=2 prevents progress bar animation, which we don't want when writing output to a file on BLT
model.fit(X_train, y_train, epochs=30, validation_data=(X_valid, y_valid), verbose=2)

# Test the network
print('\nTesting trained model:')
model.evaluate(X_test, y_test, verbose=2)
