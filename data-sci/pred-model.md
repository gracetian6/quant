# Predictive Modeling
## Classification Predictive Modeling
Approximates a mapping function (f) from input variables (X) to **discrete output variables (y)** which are often categories. 
So, the mapping function predicts the class or category for a given observation. Often predicts the probability of given
example belonging to output class. 

Variants: binary classification problem (2 classes), multi-class classification problem (3+ classes), 
multi-label classification problem (an ex assigned multiply classes)

Example: predicting probability that email is spam or not spam
Statistic: Classification Accuracy (% of correctly classified examples out of all predictions) 

## Regression Predictive Modeling
Approximates a mapping function (f) from input variables (X) to **continuous output variables (y)**

Example: predicting how much a house is predicted to sell ($100k - $200k)
Statistic: RMSE

### Conditions of Linear Regression
- Linearity
- Homoscedasticity
- Independence (sample design)
- Normality

When thinking of conditions, think about formula for linear regression. Y = beta0 + beta1 * X + eps where eps ~ N(0, sigma^2). 

If conditions aren't met, then can use robust regression.


**Regularization makes things regular or acceptable. In ML, it regularizes or shrinks coefficients towards 0. It discourages learning a more complex or flexible model to prevent overfitting.** 

### Ridge (L2) Regression (squared penalty)
Improves predictions made from new data (reduce variance) by making predictions less sensitive to the Training Data.

Ridge regression finds a new line that doesn't fit the training data as well as least squares by introducing a small 
amount of bias through penaly into how the new line is fit to the data. In return for small amount of bias, we get a 
significant drop in variance. 

***Minimizes sum of squared residuals + lambda * slope^2***

- slope^2 adds a penalty to traditional least squares method
- lambda determines how severe the penalty is
- the larger we make lambda, slope gets asymptotically close to 0 ("shrinks paramaters")

To determine value for lambda, try a bunch of values and use cross validation (10-fold cross validation) to determine
which one results in the lowest variance. 

What do we do if we have an equation with 10,001 parameters and only 500 data points? By adding 
ridge regresison penalty, we can solve for all 10,001 parameters and only 500 samples. Ridge 
Regression can find solution with cross validation and ridge regression penalty that favors small parameter
values.
- works better when most variables are useful
- tends to shrink all parameters for correlated variables together

### Lasso (L1) Regression (abs value penalty)

***Minimizes sum of squared residuals + lambda * |slope|***

Diff in shrinkage: Ridge regression can shrink the slope asymptotically close to 0 while _Lasso can shrink
the slope all the way to 0_. Since Lasso Regression can exclude useless variables form equations, it is a little better
than Ridge at reducing variance in models that contain a lot of useless variables. So, Ridge tends to do better 
when most variables are useful.
- works best when model contains a lot of useless variables
- tends to pick just one of correlated terms and eliminates others

### Elastic Net Regression
Elastic-Net Regression is combines Lasso Regression with Ridge Regression to give you the best of both worlds. It works well when there are lots of useless variables that need to be removed from the equation and it works well when there are lots of useful variables that need to be retained. And it does better than either one when it comes to handling correlated variables

***Minimizes sum of squared residuals + lambda1 * |slope| + lambda2 * slope^2***

- combines lasso regression penalty with ridge regression penalty
- good at dealing with situations with correlations between parameters

## Cross Validation

Cross Validation allows us to compare different machine learning methods and get a sense of how well they
will work in practice. 

We need to do 2 things with the data:
1) Estimate the parameters for machine learning methods (called "training the algorithm")
2) Evaluate how well the ML methods work (called "testing the algorithm")

For example, 75% data for training, 25% data for testing (4 blocks - called 4-Fold Cross Validation). 
The question then is - which 75% of the data should we use?
To determine the right blocks/data for testing, cross validation uses all blocks one at a time and sumarizes the results 
at the end. In the end, every block of data is used for testing and we can compare methods by seeing how well they performed.

Variants: Leave One Out Cross Validation (everyone is a block), 10-fold cross validation

## Dealing with Outliers
How to make model more robust to outliers?
- L1/L2 regularization (penalizes large terms / coefficients so impact on outliers is curtailed)
- Changes to Algorithm:
   - Tree Based Methods instead of regression methods (more resistant to outliers)
   - Statistical Tests: non parametric tests instead of parametric ones
   - Robust error metrics (MAE or Huber Loss instead of MSE)
- Changes to data:
  - winsorizing data (limiting extreme values to reduce effect of spurious outliers)
    - extreme values are replaced by certain percentiles (max/min percentiles) instead of discarded/trimmed 
  - transforming data (e.g. log)
  - remove outliers only if you're certain they're anomalies not worth predicting
  


### Sources
- Classification & Regression: https://machinelearningmastery.com/classification-versus-regression-in-machine-learning/
- Cross Validation: https://www.youtube.com/watch?v=fSytzGwwBVw by StatQuest with Josh Starner
- Ridge Regression: https://www.youtube.com/watch?v=Q81RR3yKn30 by StatQuest with Josh Starner
- Lasso Regression: https://www.youtube.com/watch?v=NGf0voTMlcs&t=34s by StatQuest with Josh Starner
- AUC and ROC: https://www.youtube.com/watch?v=4jRBRDbJemM by StatQuest with Josh Starner
- Logistic Regression: https://www.youtube.com/watch?v=yIYKR4sgzI8 by StatQuest with Josh Starner
- Elastic Net Regression: https://www.youtube.com/watch?v=1dKRdX9bfIo by StatQuest with Josh Starner
- Ridge vs. Lasso Regression, Visualized!!! https://www.youtube.com/watch?v=Xm2C_gTAl8c by StatQuest with Josh Starner
- Regularization Meaning: https://www.edureka.co/blog/regularization-in-machine-learning/#:~:text=In%20general%2C%20regularization%20means%20to%20make%20things%20regular%20or%20acceptable.&text=In%20the%20context%20of%20machine,flexible%20model%2C%20to%20prevent%20overfitting.
