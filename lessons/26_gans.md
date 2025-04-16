# Generative Adversarial Networks
* These are a way of generating images
* Network has two parts (Figure 17-14 from book)
  * Discriminator tries to tell real images from fake ones
  * Generator tries to fool the discriminator
  * This competition improves both of them
* Alternating phases of training
  * Train discriminator only, giving it both real images and fake ones produce by the generator
    * At first, the fake images are going to be terrible, because the generator has its random initial weights
    * The generator is not modified in this phase
  * Train the generator to fool the discriminator
    * The input to the entire network is noise; the correct output is 1 (indicating that the discriminator thinks the generated image is real)
    * The discriminator weights are frozen during this phase of training, so the generator has to produce images that will fool the current discriminator
    * Sidebar on p. 661
* TPS: Explain in plain English how you could use a GAN to generate names for pets
* [Géron's notebook](https://github.com/ageron/handson-ml3/blob/main/17_autoencoders_gans_and_diffusion_models.ipynb)
* Mode collapse (second paragraph, p. 664)
  * One solution: keep around some older fake images, so the discriminator can't forget about types of images not currently being generated
