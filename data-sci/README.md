## Data Science Plan of Attack
1. Understand High level Ideas (1-2 min)
- problem/goal
- potential problems, missing data, outliers
- plan of attack



2. Load Data
3. Inspect/Explore
- plot some histograms 
```
import matplotlib.pyplot as plt
plt.hist('col', data=train, bins=20, range=[0, 200)

df['col'].hist(bins=20, range=[0, 200])

df[['col1', 'col2']].hist()
```
- box plots of categorical variable
```train.boxplot(column='revenue', by='month')```

- TODO scatterplot
- summary, describe, info

```
df.info()
df.describe()
df.head()
```

4. Handling missing values / outliers
- ? to NaNs
```
.replace('?', np.nan)
```
- Missing values: `train.isna().sum()`
- numeric N/A
- non numeric N/A
- outliers
```
train = train.drop(np.where(train['sls'] > 300000)[0]) # the 0 index is important
train.boxplot()
```

5. Preprocessing data
- scaling features 
  - note: when scaling features, need to use the same scalar for the test data
- dummy variables
```
train = pd.get_dummies(train, columns=['col1', 'col2'], drop_first=True)
```
- `sklearn.preprocessing`
- Date Time
```
train_date = train["date"].str.split("/", expand=True)
train_date = train_date.rename(columns={0:"month", 1:"day", 2:"year"})
```

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
