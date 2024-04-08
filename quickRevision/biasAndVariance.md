# Bias and Variance


## Important Terms


## Resources


## Quick Notes | Summary
### **`Bias`**  
It refers to the error introduced by approximating a real-world problem with a simplified model. It represents the difference between the average prediction of our model and the correct value which we are trying to predict.  

**Characteristics**
- High bias models are simplistic and tend to **`underfit`** the data. They may overlook underlying patterns, resulting in poor performance on both training and testing data.
- Common causes of high bias include using linear models for nonlinear data or inadequate model complexity.  
  
**Mitigation**
- Increasing model complexity (e.g., adding more features, using a more complex model architecture).
- Using more sophisticated algorithms that can capture complex relationships in the data.


### **`Variance`**  
It measures the variability of model predictions for a given data point. It indicates how much the predictions for a given point vary across different training datasets.  

**Characteristics**
- High variance models are complex and tend to **overfit** the training data. They capture noise or random fluctuations in the training data, leading to poor generalization performance on unseen data.
- Common causes of high variance include using overly complex models or insufficient training data.  
  
**Mitigation**:
- Regularization techniques (e.g., L1, L2 regularization) to penalize large model coefficients and prevent overfitting.
- Increasing the size of the training dataset to provide more examples for the model to learn from.
- Simplifying the model architecture or reducing the number of features.

