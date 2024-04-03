# Classification


## 1. Important Terms


## 2. Resources
[Logistic Regression - skytowner](https://www.skytowner.com/explore/comprehensive_guide_on_logistic_regression)


## 3. Quick Notes | Summary

## Logistic Regression
Logistic regression is a popular classifier that predicts the probability of a binary event occurring.  

**`Note:`** The name **`"logistic regression"`** is a misnomer as this model is used for **`classification`** rather than regression.

### Bounding the output between 0 and 1 using the logit function
Logistic regression accounts for this issue and ensures that the output of the model is bounded between 0 and 1. This is done using the logit function, which is defined as follows:
$$
\text{logit}(p)=\ln \left(\frac{p}{1-p}\right)
$$

We can now define the logistic regression model for the case when we have one feature $x_1$. The logit of the probability $p$ follows a linear model:
$$
\text{logit}(p)=\ln \left(\frac{p}{1-p}\right)=\theta_0 + \theta_1*x_1
$$
$$
\hat p = \frac{e^{\theta_0 + \theta_1*x_1}}{1+e^{\theta_0 + \theta_1*x_1}}
$$
$$
\sigma(z) = \frac{e^z}{1+e^{z}} = \frac{1}{1+e^{-z}}
$$








