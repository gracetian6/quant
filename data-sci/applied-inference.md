# Applied Statistical Inference

**Inference**: Use the model to learn about the data generation process. (Model interpretability is a necessity for inference) 
- understand how ozone levels are influenced by temperature, solar radiation, and wind. 
- Goal is to explain data set as accurately as possible (so unbiased parameters good) 

**Prediction**: Use the model to predict the outcomes for new data points.
- predict future ozone levels using historic data
- Unbiased estimators not favored due to bias variance tradeoff, prioritize generalizability and avoid overfitting

## A/B Tests
- A/B test drives traffic to two different pages (control/variation) to see which version converts better
- A/A test also drives traffic to two pages to see which performs better. Pits 2 identical pages against
each other instead of two different pages. 
  - Goal: find no difference between control and variation versions / i.e. verifies sampling algorithm is random


## Testing Randomness
- plot distributions to see if same shape
- permutation test to see if distributions are the same 

## Bias Variance Tradeoff
**Bias**:  inability for ML method to capture the true relationship.
- Ex: straight line to curved dataset has a lot of bias. Squiggly line that touches all the points has very bias of 0. However, squiggly line is a lot worse for the test set.

**Variance**: the difference in fits between data sets (train and test). 
- A dataset has high variability if it results in vastly different sums of squares for different datasets. Straight line has low variance because sums of squares are similar for test and train dataset. Will give consistently good predictions (but not great). 

To get low bias and low variance, need to find the sweet spot. This can be done with regularizaiton, boosting, and bagging (rf).

## Likelihood / MLE
- Likelihood: how likely the outcome would happen given current data and model
  - probabilities are the areas under a fixed distribution 
    - Pr(data | dist)
  - Likelihoods are the y axis values for fixed data points with distributions that can be moved 
    - L(dist | data)
- MLE: finds best parameter that optimizes likelihood
  - doesn't exist for gaussian mixtures, non parametric models
- MAP: generalized version of MLE where MLE assumes uniform prior distribution of parameters. 
- MOM: solves for parameters for moments. More naive, not used over MLE since MLE more often unbiased 

### Confidence Interval
- 95% CI: Interval that contains true mean 95% of the time (assuming random sampling) 

### P-value, Type 1 & 2
- p-val: given null hypohtesis is true, its the fraction of events with parameters values more extreme than observed parameter
- type 1: reject null when it's true
- type 2: accept (fail to reject) null when it's false
- power: probability that we correctly reject the null hypothesis. Large power is good (i.e. more powerful)
  - can increase power by increasing the sample size

### Sources:
- A/B test https://vwo.com/ab-testing/
- https://github.com/kojino/120-Data-Science-Interview-Questions/blob/master/statistical-inference.md
- Inference vs Prediction: https://www.datascienceblog.net/post/commentary/inference-vs-prediction/
