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

### Ridge (L2) Regression 
Improves predictions made form new data (reduce variance) by making predictions less sensitive to the Training Data.

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

### Lasso (L1) Regression
***Minimizes sum of squared residuals + lambda * |slope|***

Diff in shrinkage: Ridge regression can shrink the slope asymptotically close to 0 while _Lasso can shrink
the slope all the way to 0_. Since Lasso Regression can exclude useless variables form equations, it is a little better
than Ridge at reducing variance in models that contain a lot of useless variables. So, Ridge tends to do better 
when most variables are useful.

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

### Sources
- Classification & Regression: https://machinelearningmastery.com/classification-versus-regression-in-machine-learning/
- Cross Validation: https://www.youtube.com/watch?v=fSytzGwwBVw by StatQuest with Josh Starner
- Ridge Regression: https://www.youtube.com/watch?v=Q81RR3yKn30 by StatQuest with Josh Starner
- Lasso Regression: https://www.youtube.com/watch?v=NGf0voTMlcs&t=34s by StatQuest with Josh Starner
- AUC and ROC: https://www.youtube.com/watch?v=4jRBRDbJemM by StatQuest with Josh Starner
- Logistic Regression: https://www.youtube.com/watch?v=yIYKR4sgzI8 by StatQuest with Josh Starner
