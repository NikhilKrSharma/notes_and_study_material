# Classification Metrices 

Various Metrices used  for classification problems.

1. **`Accuracy`**  
   - It is the ratio of correct predictions to total number of predictions.
    $$
    \text{Accuracy} = \frac{\text{True Positives + True Negatives}}{\text{Total Number of Predictions}}
    $$
2. **`Precision`:**   
   Precision is an important metrics used to evaluate the performance of classification models, especially in scenarios where the classes are imbalanced.
     - Precision measures the **accuracy of positive predictions**. 
     - It is the ratio of true positive predictions to the total number of positive predictions made by the classifier.
     - E.g., Out of all the ones which model has predicted as **`1`** how many actually are **`1`**. 
     - It is a measure of the correctness of positive.
     - It is defined as the ratio of correctly predicted positive observations to the total predicted positives.
3. **`Recall`:**   
   Recall is an important metrics used to evaluate the performance of classification models, especially in scenarios where the classes are imbalanced.
     - Recall, also known as sensitivity or true positive rate. 
     - It is the ratio of true positive predictions to the total number of actual positive instances in the dataset.
     - E.g., Out of all the **`1`** how many our model has predicted as **`1`**.

**`Note`**: It's important to note that **`precision`** and **`recall`** are often inversely related; improving one may lead to a decrease in the other. Therefore, finding the right balance between precision and recall is crucial depending on the specific requirements of the task at hand.

4. **`F1 Score`**  
   - The F1 score is particularly useful in situations where you want to balance the trade-off between **`precision`** and **`recall`**. Here are some scenarios where you might consider using the F1 score.  
   - F1 score, is the harmonic mean of precision and recall. It provides a single metric that balances both precision and recall.
    $$
    F1 = 2 \times \frac{precision * recall}{precision + recall}
    $$





   