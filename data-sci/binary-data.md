# Binary Predictive Modeling

### Logistic Regression
Fits an s shaped curve to binary output data (is obese/not obese). The y axis on the curve tells you the probability that the mouse is obese. 

Instead of minimizing least sqs, fits curve with **maximum likelihood**. You pick a probability, scaled by weight, of observing an obese mouse.
You use that to calculate the likelihood for all the data points and multiply all of these. The likelihood of the data gives you a line, and 
you calculate many likelihoods and select curve w the maximum likelihood for the logistic curve.


### AUC and ROC for measure how good a Binary Classifier
ROC curves make it easy to identify the best threshold for making a decision (i.e. whether threshold for obesity should prob of 0.9 or 0.5). 
Plots false positive rate on x axis and true positive rate on y axis. 

The AUC (area under curve) can help you determine which categorization method is better. (Larger AUC is better). 

Con: Can't interpret predictions as probabilities because AUC is determined by rankings, so can't explain uncertainty of model.

### SVM

The shortest distance between the observations and the threshold is called the **margin**. When we use the threshold that gives 
us the largest margin to make classifications, we are using the maximal marginal classifier. (bad because super sensitive to outliers)

Support Vector Classifier comes from the fact that the observations on the edge and within the soft margin are called support vectors.

### Naive Bayes

### Decision Tree

## Deep Learning 

### Sources 
- AUC and ROC: https://www.youtube.com/watch?v=4jRBRDbJemM by StatQuest with Josh Starner
- Logistic Regression: https://www.youtube.com/watch?v=yIYKR4sgzI8 by StatQuest with Josh Starner
- SVM Part 1: https://www.youtube.com/watch?v=efR1C6CvhmE by StatQuest with Josh Starner
