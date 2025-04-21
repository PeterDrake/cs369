# Transformers
* Word embeddings
  * [Pimantle](https://semantle.pimanrul.es/)
  * Word2vec associates words with similar context with similar high-dimensional vectors
  * king - man + woman = queen
  * Bias problem: doctor - man + woman = nurse
* [Attention](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)
* Transformers
  * Meant to deal with exploding/vanishing gradient problem
  * Also allow entire string to be processed in parallel
  * Short story: use attention to, for each word, look at the whole input string (up to the point of the word in question)
