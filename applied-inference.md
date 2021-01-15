# Applied Statistical Inference

Inference: Use the model to learn about the data generation process. (Model interpretability is a necessity for inference) 
- understand how ozone levels are influenced by temperature, solar radiation, and wind

Prediction: Use the model to predict the outcomes for new data points.
- predict future ozone levels using historic data

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
- Inference vs Prediction: https://www.datascienceblog.net/post/commentary/inference-vs-prediction/
