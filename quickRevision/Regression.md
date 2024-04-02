# Regression

## Important Terms
Assumptions, Linear, Multiple, Polinomial, Ridge (L2), Laso (L1), Elastic Net, Linearity, Normality, Homoscedasticity, Multicolinearity, Error Distribution, MSE, RMSE, R<sup>2</sup>.


## Resources
- [Analytics Vidhya - Linear Regression](https://www.analyticsvidhya.com/blog/2021/05/all-you-need-to-know-about-your-first-machine-learning-model-linear-regression/, 'Linear Regression')
- [How to transform features into Normal/Gaussian Distribution](https://www.analyticsvidhya.com/blog/2021/05/how-to-transform-features-into-normal-gaussian-distribution/)
- [Simple linear regression - Sky Towner](https://www.skytowner.com/explore/introduction_to_linear_regression)
- [Linear Regression With Gradient Descent From Scratch - Medium](https://medium.com/@shuklapratik22/linear-regression-with-gradient-descent-from-scratch-d03dfa90d04c)

## Quick Notes | Summary
- **Types of Linear Regression**
    - **`Simple Linear Regression`**  
    In simple linear regression, there is only one independent variable that is used to predict the dependent variable.

    - **`Multiple Linear Regression`**  
    Multiple linear regression extends simple linear regression to multiple independent variables. It models the relationship between the dependent variable and two or more independent variables. The equation of the model becomes a linear combination of the independent variables.

    - **`Polynomial Linear Regression (Non-Linear)`**  
    Polynomial regression is a form of regression analysis in which the relationship between the independent variable `x` and the dependent variable `y` is modeled as an `nth` degree polynomial. It allows for more flexible modeling of non-linear relationships.

    - **`Ridge Regression (L2 Regularization)`**  
    Ridge regression is a regularization technique used to prevent overfitting in linear regression models. It adds a penalty term to the standard linear regression objective function, which penalizes large coefficients. This helps to reduce model complexity and variance.

    - **`Lasso Regression (L1 Regularization)`**  
    Lasso regression is another regularization technique used in linear regression models. Similar to ridge regression, it adds a penalty term to the objective function. However, lasso regression uses the absolute values of the coefficients as the penalty term. This leads to sparsity in the coefficient values, effectively performing feature selection.

    - **`Elastic Net Regression`**  
    Elastic net regression combines the penalties of ridge and lasso regression. It adds both the `L1` and `L2` penalty terms to the objective function, allowing for a more flexible regularization approach.

- **Assumptions of Linear Regression**
    - **`Linearity`**  
    It states that the independent variable X should be linearly related to the independent variable Y. This assumption can be checked by plotting a scatter plot between both variables.

    - **`Normality`**  
    The X and Y variables should be normally distributed. Histograms, KDE plots, Q-Q plots can be used to check the Normality assumption. 

    - **`Homoscedasticity`**  
    The variance of the error terms should be constant i.e the spread of residuals should be constant for all values of X. This assumption can be checked by plotting a residual plot. If the assumption is violated then the points will form a funnel shape otherwise they will be constant.

    - **`Independence/No Multicollinearity`**  
    The variables should be independent of each other i.e no correlation should be there between the independent variables. To check the assumption, we can use a correlation matrix or VIF score. If the VIF score is greater than 5 then the variables are highly correlated.

    - The **`error terms should be normally distributed`**. Q-Q plots and Histograms can be used to check the distribution of error terms.


<br>

- [**How to deal with the `Violation of any of the Assumption`**](https://www.analyticsvidhya.com/blog/2021/05/how-to-transform-features-into-normal-gaussian-distribution/)


## Cost Function of Regression Model
The cost function is the objective function that we want to minimize in order to find the best parameters for our regression model. The cost function is a measure of the error between actual values and the predicted values in our regression model. 

$$
\text{J}(\beta) = \frac{1}{2} * \sum_{i=1}^{n}(y_i - \hat{y}_n)^2
$$
#### Q. What is the purpose of squaring the difference
If we did not include the square term here, then the error terms would simply cancel each other out, and hence the cost function will be equal 0, indicating a perfect fit but its not the case in reality.

#### Q. Squaring versus taking absolute value
1. Taking the absolute value $\mid y_i -\hat{y}_i\mid$ does remove negative differences.
2. Taking the absolute value is a better measure of error because squaring the differences inflates the cost function.  
   
BUT
1. Absolute values don't work well with derivatives, and this becomes a problem later on when we compute the derivative of the cost function.
2. It also does not matter if the cost value gets inflated due to the squaring because:
   - We are typically concerned with finding the parameters that minimize the error, that is, the final value of the cost function is less important.
   - We can still objectively compare the performance of two linear regression models as long as we use the same cost function.

