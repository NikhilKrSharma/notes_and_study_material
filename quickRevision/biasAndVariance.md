# Bias and Variance


## Important Terms


## Resources


## Quick Notes | Summary
### **`Bias`**  
High bias means the model is too simple and cannot capture the underlying structure of the data, leading to systematic errors. 

In simpler terms, bias is like **`underfitting`** - the model is too simple and misses important patterns. 

**Characteristics**
- High bias models are simplistic and tend to **`underfit`** the data. They may overlook underlying patterns, resulting in poor performance on both training and testing data.
- Common causes of high bias include using linear models for nonlinear data or inadequate model complexity.  
  
**Mitigation**
- Increasing model complexity (e.g., adding more features, using a more complex model architecture).
- Using more sophisticated algorithms that can capture complex relationships in the data.


### **`Variance`**  
High variance indicates that the model is overly sensitive to fluctuations in the training data and captures noise along with the underlying patterns.  

In simpler terms, variance is like **`overfitting`** - the model captures noise along with the patterns, making it perform well on the training data but poorly on new, unseen data.

**Characteristics**
- High variance models are complex and tend to **overfit** the training data. They capture noise or random fluctuations in the training data, leading to poor generalization performance on unseen data.
- Common causes of high variance include using overly complex models or insufficient training data.  
  
**Mitigation**:
- Regularization techniques (e.g., L1, L2 regularization) to penalize large model coefficients and prevent overfitting.
- Increasing the size of the training dataset to provide more examples for the model to learn from.
- Simplifying the model architecture or reducing the number of features.

