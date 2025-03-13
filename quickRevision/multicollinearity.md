# Multicollinearity

## 1. Important Terms
lorem iposum

## 2. Resources
- [Analytics Vidhya - Multicollinearity | Causes, Effects and Detection](https://www.analyticsvidhya.com/blog/2020/03/what-is-multicollinearity/)

## 3. Quick Notes | Summary
- **`What is Multicollinearity`**  
  Multicollinearity is a statistical phenomenon that occurs when two or more independent variables in a multiple regression model are highly correlated with each other.

  This can create challenges in the regression analysis because it becomes difficult to determine the individual effects of each independent variable on the dependent variable accurately.
  
  Multicollinearity can lead to unstable and unreliable coefficient estimates, making it harder to interpret the results and draw meaningful conclusions from the model.

  When two variables have a correlation coefficient of either `+1` or `-1`, they are considered perfectly collinear.

- **`Detection of Multicollinearity`**
  - Correlation matrix: Calculate the correlation coefficients between predictor variables. Correlation values close to 1 or -1 indicate high multicollinearity.
  
  - Variance Inflation Factor (VIF): Calculate the VIF for each predictor variable. VIF measures how much the variance of an estimated regression coefficient is increased due to multicollinearity. VIF values above 10 or 5 indicate multicollinearity.
  
  $$\text{VIF}_j = \frac{1}{1 - R_j^2}$$
  
  - Eigenvalues: Calculate the eigenvalues of the correlation matrix. Small eigenvalues indicate multicollinearity.
   
- **`Fixing Multicollinearity`**
  - Remove redundant variables: Remove one of the correlated predictor variables from the model, especially if they represent similar information.
  
  - Feature selection: Use techniques like forward selection, backward elimination, or stepwise regression to select a subset of predictor variables that minimizes multicollinearity.
  
  - Combine variables: Create composite variables or interaction terms to represent the combined effect of correlated predictors.
  
  - Regularization: Use regularization techniques like ridge regression or Lasso regression, which penalize large coefficients and mitigate multicollinearity. 

<br>

- **`Key Takewayas`**
1. Multicollinearity occurs when two or more independent variables have a high correlation with one another in a regression model, which makes it difficult to determine the individual effect of each independent variable on the dependent variable.
   
2. Multicollinearity can occur due to poorly designed experiments, highly observational data, creating new variables that are dependent on other variables, including identical variables in the dataset, inaccurate use of dummy variables, or insufficient data.
   
3. One method to detect multicollinearity is to calculate the variance inflation factor (VIF) for each independent variable, and a VIF value greater than 1.5 indicates multicollinearity.
   
4. To fix multicollinearity, one can remove one of the highly correlated variables, combine them into a single variable, or use a dimensionality reduction technique such as principal component analysis to reduce the number of variables while retaining most of the information.