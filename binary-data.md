# Binary Predictive Modeling

### Logistic Regression
Fits an s shaped curve to binary output data (is obese/not obese). The y axis on the curve tells you the probability that the mouse is obese. 

Instead of minimizing least sqs, fits curve with **maximum likelihood**. You pick a probability, scaled by weight, of observing an obese mouse.
You use that to calculate the likelihood for all the data points and multiply all of these. The likelihood of the data gives you a line, and 
you calculate many likelihoods and select curve w the maximum likelihood for the logistic curve.


### AUC and ROC for Binary Classifiers
ROC curves make it easy to identify the best threshold for making a decision (i.e. whether threshold for obesity should prob of 0.9 or 0.5). 
Plots false positive rate on x axis and true positive rate on y axis. 

The AUC (area under curve) can help you determine which categorization method is better. (Larger AUC is better). 

Con: Can't interpret predictions as probabilities because AUC is determined by rankings, so can't explain uncertainty of model.

### SVM
