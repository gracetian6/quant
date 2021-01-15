# Applied Statistical Inference

Inference: Given a set of data you want to infer how the output is generated as a function of the data.

Prediction: Given a new measurement, you want to use an existing data set to build a model that reliably chooses the correct identifier from a set of outcomes.

Inference: You want to find out what the effect of Age, Passenger Class and, Gender has on surviving the Titanic Disaster. You can put up a logistic regression and infer the effect each passenger characteristic has on survival rates.

Prediction: Given some information on a Titanic passenger, you want to choose from the set {lives,dies} and be correct as often as possible. (See bias-variance tradeoff for prediction in case you wonder how to be correct as often as possible.)

## Tests
- A/B test drives traffic to two different pages (control/variation) to see which version converts better
- A/A test also drives traffic to two pages to see which performs better. Pits 2 identical pages against
each other instead of two different pages. 
  - Goal: find no difference between control and variation versions / i.e. verifies sampling algorithm is random


## Testing Randomness
- plot distributions to see if same shape
- permutation test to see if distributions are the same 

## Likelihood / MLE
- Likelihood: how likely outcome would happen given current data and model
- MLE: finds best parameter that optimizes likelihood
  - doesn't exist for gaussian mixtures, non parametric models
- MAP: generalized version of MLE where MLE assumes uniform prior distribution of parameters. 
- MOM: solves for parameters for moments. More naive, not used over MLE since MLE more often unbiased 

### Confidence Interval
- 95% CI: Interval that contains true mean 95% of the time (assuming randomn sampling) 

### Sources:
- A/B test https://vwo.com/ab-testing/
- https://github.com/kojino/120-Data-Science-Interview-Questions/blob/master/statistical-inference.md
- Inference vs Prediction: https://stats.stackexchange.com/questions/244017/what-is-the-difference-between-prediction-and-inference#:~:text=Inference%3A%20Given%20a%20set%20of,from%20a%20set%20of%20outcomes.
