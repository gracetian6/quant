# Data Analysis
## Curse of Dimensionality
As the number of features or dimensions grows, the amount of data we need to generalize accurately grows exponentially. 

1. If we have more features than obs then we run into the risk of massively overfitting our model.
2. With too many features, observations become harder to cluster / no meaningful clusters can be formed. 
Too many dimensions causes every observation in your dataset to appear equidistant form all the others. 
Clustering is important because it quantifies the similarity between observations... 

## More Data?
Statistically - having more data doesn't help. Also, if model has high bias, then getting more data doesn't improve the fundamental problems of model.
There are also issues with storage, memory, etc. 

## Exploratory Data Analysis
Explatory phase to graph things, test things on small sets of data, summarizing simple statistics, getting rough ideas of what 
hypotheses you might want to pursue further. Then alternate between looking at lot of hypotheses. 

Balance of the two prevents you from wasting too much time on things that end up meaningless. 

## Selecting Important Variables
- p values of linear regression
- generate plots of relative important in random forest for each feature 
- variables added in forward variable selection
- select variables with LASSO -- forces coefficients of "not-so-signficant" variables to become 0 through penalty

## Multi-collinearity 
- use principal component analysis (PCA) to resolve the issue 

## Random Forests
Random Forests combine simplicity of decision trees with flexibility resulting in a vast improvement in accuracy. 

Process: Bootstrapped sample, subset of variables at each step for tree, so many trees. 
To predict data, we run the data for all the trees we have to determine whether patient has heart disease or not. 

Bagging: Bootstrapping the data + using aggregate to make decision. Use this data to test whether all the other trees are good / correctly label
the data set. Accuracy of our random forest is determined by proportion of out of bag samples that were correctly classified by random forest.

Out of Bag Dataset: Data set entries that were not selected in bootstrap. 

We can test many different features (number of variables used per step), and then choose which random forest works.

Random forests also deals with missing data and sample clustering. 
### Random Forests and Missing Data
- For original dataset used to create random forest:

Proximity Table measures overlap between samples and same random forest results. The values that are similar helps give us guesses
about the missing data.

- For new sample:
Use iterative method above to fill in missing values for predictors. Test the same data row with YES and NO separately for heart disease, choose the 
sample that was correctly labeled more in the random forest. 

## Sources
- https://www.youtube.com/watch?v=QZ0DtNFdDko
- Curse of Dimensionality: https://towardsdatascience.com/the-curse-of-dimensionality-50dc6e49aa1e?gi=ac56e4ff5cdd
- Lasso Variable Selection: https://towardsdatascience.com/variable-selection-using-lasso-493ac2e5660d
- Random Forest: https://www.youtube.com/watch?v=J4Wdy0Wc_xQ
