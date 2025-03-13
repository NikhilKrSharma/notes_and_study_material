# Customer Scorecard Modeling

## 1. Important Terms
Assumptions, Linear, Multiple, Polinomial, Ridge (L2), Laso (L1), Elastic Net, Linearity, Normality, Homoscedasticity, Multicolinearity, Error Distribution, MSE, RMSE, R<sup>2</sup>.


## 2. Resources
- [Credit Scoring](https://www.youtube.com/watch?v=M_iaBcLEN-8)

## 3. Quick Notes | Summary
1. **`Credit History`**  
   - Credit history is a person's premanent record related to finace (e.g. car loans, student loans, credit cards etc.)  
   - 7 to 8 years rolling history of once's payment

2. **`Credit Score`**  
   - A number that indicates a consumer's credit worthiness to lenders.
   - Measure of how risky you are to the creditor/lender.
   - Measure ho much lender can make of off you.
   - Generally the credit score range lies in 300-900
     - 851 - 900 : Excellent
     - 751 - 850 : Good
     - 651 - 750 : Average
     - 501 - 650 : Poor
     - 300 - 500 : Very Poor 

3. **`Credit Bureau's in India`**  
   There are multiple  Credit Bureaus operating in India, and they all are regulated by  **RBI** (Reserve Bank of India) under **Credit Information Companies (Regulation) Act 2005**.
   1.  Experian
   2.  Trans Union (CIBIL)
   3.  Equifax
   4.  CRIF High Mark  
   
   CB (Credit Bureau) or CIC (Credit Information Companies) are responsible for evaluating credit worthiness of the individual. It uses various informations such as your past re-payment history, credit utilisation, outstanding debts etc. to prepare your **`redit report`** and issue a **`credit score`** based on these pieces of information.

4. **`Credit Rating Agencies`**  
   They are responsible for evaluating the credit worthiness of business entities such as sole properitership, public and private companies etc. They use funantial details such as sales, debts, profit etc. to give credit ratings to the entities. They are regulated by **SEBI**.  

   Some Credit Rating Agencies operating in India are:
   - Acuite Ratings & Research Ltd.
   - Brickwork Ratings India Pvt. Ltd.
   - CARE Ratings Ltd.
   - CRISIL Ratings Ltd.
   - ICRA Limited.
   - Indian Ratings & Research Pvt. Ltd. (Formerly Fitch Rating India Pvt. Ltd.)
   - Infomerics Valuation & Rating Pvt. Ltd.

5. Key Factors considered in **`Conventional Credit Scores model`**  
   1. Payment history
   2. Amount of Debt (Ratio) [Rule of thumb, **Credit Utilisation < 30% of Credit Limit**]
   3. Length of credit history
   4. Credit Mix
   5. Credit Inquiries (Hard and Soft Enquiries)

6. **`Score Card`**  
   - Scores are given for each metrices/features selected for the scorecard.
   - **`WHY`**  
     - Easy to interpret to people without advance knowledge of statistics or data mining.
     - Reasons for declines, low scores or high scores can be explained easily.
     - Development preocess is standard and widely understood.
     - Easy to diagnose and monitor using standard reports.  
        | Charecterstics/Features | Atrribute | Scorecard Point |
        | :---------------- | :------- | ----: |
        | Age | Age < 22 | 100 |
        | Age | 22 <= Age < 20 | 120 |
        | Age | 26 <= Age < 29 | 150 |
        | Home | Own | 225 |
        | Home | Rented | 110 |
        | Income | Income < 10000 | 140 |
        | Income | 10000 <= Income < 20000 | 160 |

7. Steps involved in **`Scorecard Modeling`**  
   1. Feature Discretization
   2. Feature Selection
   3. Feature Transformation
   4. Logistic Regression
   5. Scoring Algorithm
   6. Scaling

<br>

-----  

<br>

1. **`Feature Discretization`**  
   Reduces the no. of values by grouping them in a number of intervals or bins.
   - Supervised Discretization
   - Un-supervised Discretization
   - Equal Interval WIdth: Divides the range of attribute values into `N` intervals of equal width.
   - Equal Frequency: Divides the range into `N` intervals. Each containing same number of observations.
   - Clustering Approach (K-means): Grouping the observations into k-clusters in which each observation belongs to the cluster with the nearest centroid.

2. **`Feature Selection`** 
   - Feature selection is done typically by using [**`Information Value (IV) and Weight of Evidence (WoE)`**](./IV_and_WoE.md) for scorecard applications.
  
   - **Weight of Evidence (WoE)**
     - It measures the **`strength of each bin (attribute)`** in separating good and bad examples.
  
      $$
      \text{WoE} = \ln\left(\frac{\% \text{ Non-events}}{\% \text{ Events}}\right) * 100
      $$

     - Negative values indicate that a particular bin has a higher proportion of bad applicants than good applicants.

   - **Information Value (IV)**
        - All continious predictors are categorised.
        - Missing data is considered as a separate category.
        - It measures the **`total strength of the variable`**.  
            Summation(i=1, n) [(Good Distribution - Bad Distribution) * ln(Good/Bad)]
        - It can be used to rannk and select variables very quickly.

3. **`Feature Transformation`** 
   - Transform original data into WoE.
   - Two Step process
     1. Splitting/Grouping
        - Continious Variables: Split each variable into few bins.
        - Discrete Variable: Leave them of group each variable into few categories.
     2. Caluclate WoE values of each bin (category) and replace variable value by WoE values.

4. **`Logistic Regression`**
   $$
   \sigma(z) = \frac{1}{1 + e^{-z}}
   $$

   $$
   P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X_1 + \beta_2 X_2 + \ldots + \beta_n X_n)}}
   $$

5. **`Scoring Algorithm`**  
   - Unscalled score for an individual **`i`**  
      $$
      s = \theta_0 + \theta_1 \times \text{WoE}_1(i) + \theta_2 \times \text{WoE}_2(i) + \ldots + \theta_n \times \text{WoE}_n(i)
      $$
   - The score of an individual is given by the  
      $$
      Score(p) = \text{Shift} + \text{Slope} * [\theta_0 + \theta_1 \times \text{WoE}_1(i) + \theta_2 \times \text{WoE}_2(i) + \ldots + \theta_n \times \text{WoE}_n(i)]
      $$
   - Shift and Slope: Scaling constants, making scores to conform to a particular range of scores.

6. **`Scaling`**  
   - One fo the most common setting is that the **odds doubling at every 20 points**.  
      **`PDO`**: Points to Double the Odds

   - Shift and Slope can be calculated by:  
      $$
      \text{Points} = \text{Shift}+\text{Slope}*\ln(odds)  
      $$
      $$
      \text{Points}+\text{pdo} = \text{Shift}+\text{Slope}*\ln(2*odds)  
      $$
   - Solving for PDO  
      $$
      \text{pdo} = \text{Slope}*\ln(2)  
      $$
      $$
      \text{Slope} = \frac{pdo}{ln(2)}
      $$
      $$
      \text{Shift} = \text{Points}-\text{Slope}*\ln(odds)  
      $$
   - Example: A scorecard being scalled to have  
      1. Odds of 50:1 at 600 points
      2. Odds to double every 20 points
      3. Slope & Shift

      Sollution:
      $$
      \text{Slope} = \frac{20}{ln(2)} = 28.8539
      $$
      $$
      \text{Shift} = 600-28.8539*ln(50/1) = 487.123
      $$
      $$
      \text{Points} = 487.123+28.8539*ln(\text{Odds})
      $$

      