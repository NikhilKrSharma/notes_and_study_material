# Big Data


## Important Terms


## Resources


## Quick Notes | Summary

### Euclidean Distance:

Euclidean distance is the straight-line distance between two points in Euclidean space. It's the most common distance metric and is calculated using the Pythagorean theorem.

**Formula**:
The Euclidean distance between two points \( P \) and \( Q \) in \( n \)-dimensional space is given by:

\[ \text{Euclidean distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + \ldots + (z_2 - z_1)^2} \]

**Example**:
Consider two points \( P \) and \( Q \) in 2-dimensional space:

- Point \( P \): \( (1, 2) \)
- Point \( Q \): \( (4, 6) \)

Using the Euclidean distance formula:

\[ \text{Euclidean distance} = \sqrt{(4 - 1)^2 + (6 - 2)^2} \]
\[ = \sqrt{3^2 + 4^2} \]
\[ = \sqrt{9 + 16} \]
\[ = \sqrt{25} \]
\[ = 5 \]

So, the Euclidean distance between points \( P \) and \( Q \) is 5.

---

### Manhattan Distance:

Manhattan distance, also known as city block distance or taxicab distance, measures the distance between two points along the axes at right angles. It's named after the grid-like layout of streets in Manhattan.

**Formula**:
The Manhattan distance between two points \( P \) and \( Q \) in \( n \)-dimensional space is given by:

\[ \text{Manhattan distance} = |x_2 - x_1| + |y_2 - y_1| + \ldots + |z_2 - z_1| \]

**Example**:
Consider two points \( P \) and \( Q \) in 2-dimensional space:

- Point \( P \): \( (1, 2) \)
- Point \( Q \): \( (4, 6) \)

Using the Manhattan distance formula:

\[ \text{Manhattan distance} = |4 - 1| + |6 - 2| \]
\[ = |3| + |4| \]
\[ = 3 + 4 \]
\[ = 7 \]

So, the Manhattan distance between points \( P \) and \( Q \) is 7.

---

### Minkowski Distance:

Minkowski distance is a generalized distance metric that includes both Euclidean distance (p = 2) and Manhattan distance (p = 1) as special cases. It's defined as:

\[ \text{Minkowski distance} = \left( \sum_{i=1}^{n} |x_{2i} - x_{1i}|^p \right)^{\frac{1}{p}} \]

**Example**:
Consider two points \( P \) and \( Q \) in 2-dimensional space:

- Point \( P \): \( (1, 2) \)
- Point \( Q \): \( (4, 6) \)

Using the Minkowski distance formula with \( p = 3 \) (just as an example):

\[ \text{Minkowski distance} = \left( |4 - 1|^3 + |6 - 2|^3 \right)^{\frac{1}{3}} \]
\[ = \left( 3^3 + 4^3 \right)^{\frac{1}{3}} \]
\[ = \left( 27 + 64 \right)^{\frac{1}{3}} \]
\[ = \left( 91 \right)^{\frac{1}{3}} \]
\[ \approx 4.497 \]

So, the Minkowski distance between points \( P \) and \( Q \) with \( p = 3 \) is approximately 4.497.


## Choice of Distance Metrices
The choice of distance metric, whether it's Euclidean, Manhattan, Minkowski, or others, depends on the characteristics of the data and the specific requirements of the problem at hand. Here are some guidelines on when to use each distance metric:

Euclidean Distance:
Use Case: Euclidean distance is suitable when the data is continuous and the concept of straight-line distance is relevant.
Example Applications: Image processing, pattern recognition, feature extraction.
Manhattan Distance:
Use Case: Manhattan distance is useful when the data is in a grid-like structure or when movement can only occur along axes.
Example Applications: Taxicab routing, network routing, grid-based games.
Minkowski Distance:
Use Case: Minkowski distance is a generalization that includes both Euclidean distance (p = 2) and Manhattan distance (p = 1). It's versatile and can be used in various scenarios.
Example Applications: When you want to try different distance metrics and evaluate which one works best for your specific problem. It's also commonly used in machine learning algorithms like KNN, where you can experiment with different values of 
p
p to find the most suitable distance metric.
Other Distance Metrics:
Chebyshev Distance: Suitable for scenarios where movement is allowed in all directions with equal cost.
Cosine Similarity: Useful for measuring similarity between vectors, particularly in high-dimensional spaces.
Hamming Distance: Applicable when dealing with categorical data or binary strings.
Jaccard Similarity: Effective for measuring similarity between sets or binary vectors.
When choosing a distance metric, it's essential to consider the nature of the data, the problem requirements, and the computational complexity of the distance calculation. Experimentation and validation using appropriate evaluation metrics are crucial to determine the most suitable distance metric for a specific task.