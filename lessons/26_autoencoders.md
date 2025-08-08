# Autoencoders
* Idea: Train a network to output its input (unsupervised learning)
* Why?
  * Dimensionality reduction
  * Visualization
  * Pretraining
  * Denoising
* Crucial: The innermost hidden layer is smaller than the input and output layers, so this isn't a trivial "pass-through"; the network has to learn key features
  * Activity: If you had to represent a grayscale image of a face into four floats in [0, 1], what would they be?
  * Chess memorization experiment
* Work through [Géron's workbook](https://github.com/ageron/handson-ml3/blob/main/17_autoencoders_gans_and_diffusion_models.ipynb)