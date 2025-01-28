

https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/






# RNN-Seq2sec-Transformers

## Important Terms




## Resources
- [Analytics Vidhya - Linear Regression](# Regression

## Important Terms
Assumptions, Linear, Multiple, Polinomial, Ridge (L2), Laso (L1), Elastic Net, Linearity, Normality, Homoscedasticity, Multicolinearity, Error Distribution, MSE, RMSE, R<sup>2</sup>.


## Resources
- [Visualizing A Neural Machine Translation Model - Mechanics of Seq2seq Models With Attention](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/, 'Linear Regression')

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)




## Word Embeddings
- **`GloVe`** (Global Vectors for Word Representation) and **`word2vec`** are both popular algorithms used for generating word embeddings.
  
| Feature                   | Word2Vec                                    | GloVe                                     |
|---------------------------|---------------------------------------------|-------------------------------------------|
| **Algorithm**             | Neural networks (CBOW, Skip-Gram)           | Matrix factorization                      |
| **Context**               | Local (fixed window)                        | Global (entire corpus)                    |
| **Data Representation**   | Raw text data                               | Co-occurrence matrix                      |
| **Efficiency**            | Faster, suitable for online training        | More computationally intensive            |
| **Mathematical Foundation**| Neural network-based                       | Matrix factorization-based                |
| **Interpretability**      | Implicit relationships                      | Explicit relationships                    |

- [The amazing power of word vectors](https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors/)
- [Bag of Words Meets Bags of Popcorn - Check Once](https://www.kaggle.com/competitions/word2vec-nlp-tutorial)
- The Big Idea of Word Embedding is to turn text into numbers.
- Word Embedding is used to map words or phrases from a vocabulary to a corresponding vector of real numbers.
- Word Embedding aims to create a vector representation with a much lower dimensional space. These are called Word Vectors.
- **`Word Embedding`** is a low-dimensional vector representation from corpus of text, which preserves the contextual similarity of words.
- There are two ways to implement word2vec:
  -  CBOW (Continuous Bag-Of-Words): Here we predict the word around a context.
  -  Skip-gram: Here we predict the context around a word.






## Quick Notes | Summary
- **`Seq2seq Model`**: Under the hood, the model is composed of an **encoder** and a **decoder**.
  - **Encoder**: The encoder processes each item in the input sequence, it compiles the information it captures into a vector (called the **context**).
  - **Decoder**: The decoder, which begins producing the output sequence item by item.
  - The encoder and decoder tend to both be recurrent neural networks.
  - Context Vector: In real world applications the context vector would be of a size like 256, 512, or 1024.
- An **attention model** differs from a **classic sequence-to-sequence model** in two main ways:
  - First, the encoder passes a lot more data to the decoder. Instead of passing the last hidden state of the encoding stage, the encoder passes all the hidden states to the decoder
  - Second, an attention decoder does an extra step before producing its output. In order to focus on the parts of the input that are relevant to this decoding time step, the decoder does the following:
    - Look at the set of encoder hidden states it received – each encoder hidden state is most associated with a certain word in the input sentence.
    - Give each hidden state a score (let’s ignore how the scoring is done for now)
    - Multiply each hidden state by its softmaxed score, thus amplifying hidden states with high scores, and drowning out hidden states with low scores.




## Transformers
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- Input >>> TRANSFORMER >>> Output
- Transformer = Encoding Component + Decoding Component
- Encoding Component = The encoding component is a stack of encoders (the paper stacks six of them on top of each other)
- Decoding Component = The decoding component is a stack of decoders of the same number.
- The encoders are all identical in structure (yet they do not share weights).
- Each Encoder is broken down into two sub-layers:
  - Self Attention Layer: This layer that helps the encoder look at other words in the input sentence as it encodes a specific word.
  - Feed Forward Neural Layer: The exact same feed-forward network is independently applied to each position.
- Each Decoder can also be broken down in 3  sub-layers:
  -  Self Attention Layer
  -  Encoder Decoder Attention: The attention layer helps the decoder focus on relevant parts of the input sentence (similar what attention does in seq2seq models).
  -  Feed Forward Neural Layer