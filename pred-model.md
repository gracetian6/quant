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
