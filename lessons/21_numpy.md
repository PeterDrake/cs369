***Bring NumPy cheat sheets***

# NumPy
* Numpy is a package for manipulating arrays of numbers
  * Vastly more efficient in both space and time
  * Many things can be done with much less code
* Creating a numpy array
* Differences from plain Python lists
  * Fixed size
  * Fixed data type
    * See with the dtype attribute
    * Specify when creating array with optional dtype argument
    * [List of types](https://numpy.org/doc/stable/user/basics.types.html)
  * Potentially multidimensional
* Multidimensional arrays
  * Creating from nested lists
  * Accessing elements: a[2, 3]
  * Creating with zeros
    * Specify shape as a tuple
* Class challenge: create a 10x10 smiley face
* Attributes of a Numpy array: ndim, shape, size, dtype
* Slicing
  * One dimension: just like lists
  * Multiple dimensions: provide a slice for each dimension
  * Class challenge: create 9x9 array with concentric squares, alternating 1 and 0
  * Unlike lists, NumPy slices do not copy the array!
    * You can do so with the copy method
* Reshaping
* Concatenating
* Class challenge: create a checkerboard
* Operations
  * Element-wise operations
    * Avoid loops!
    * Broadcasting
      * Left-pad lower-dimensional shape with 1s
      * Stretch any 1s
        * If you can't (e.g., 3 vs 5), raise an error
  * Functions across axes (sum, etc.)
  * Comparisons
  * Matrix multiplication with `@`
* Now, for updating activation of an entire layer of a neural network, it's just `logistic(inputs @ weights)`
  * This assumes:
  ```python
  def logistic(x):
    return 1/(1+np.exp(x))
  ```
  * More is needed to handle biases (either concatenate them to the inputs or add biases after the matrix multiplication)
  * Backpropagation is trickier
