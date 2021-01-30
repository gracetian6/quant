## Data Science Plan of Attack
1. Understand High level Ideas (1-2 min)
- problem/goal
- potential problems, missing data, outliers
- plan of attack
2. Load Data
3. Inspect/Explore
- plot some histograms, 
- summary, describe, info
4. Handling missing values / outliers
- ? to NaNs
- numeric
- non numeric
5. Preprocessing data
- scaling features 
  - note: when scaling features, need to use the same scalar for the test data
- dummy variables
- `sklearn.preprocessing`
6. Fiting model
- logistic for classification
- regression for quantitative variables
  - consider linear regression assumptions, forward variable selection, transforming data/hist plots
7. Make predictions and evalute preformance
- for logistic regression, do a confusion matrix
  - want high numbers on diagonals
8. Find best performing model
- Grid search to tune hyper parameters, pick the best lambdas
- cross validation
- Ridge/Lasso to pick better variables 
