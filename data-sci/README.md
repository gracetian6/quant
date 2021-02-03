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
PAIR PLOT
```
import seaborn as sns
sns.pairplot(train[['col1', 'col2', 'category']], hue='category', corner=True)
plt.show()
```

SCATTER PLOT
```
plt.plot('col1', 'col2', 'o', data=train, markersize=4)
plt.xlabel('col1')
plt.ylabel('col2')
plt.show()
```

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
```
df['col'].replacena() # TODO check
```
- non numeric N/A
- outliers
```
train = train.drop(np.where(train['sls'] > 300000)[0]) # the 0 index is important
train.boxplot()
```

5. Preprocessing data
- scaling features 
  - note: when scaling features, need to use the same scalar for the test data

# Import MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
```
# Instantiate MinMaxScaler and use it to rescale X_train and X_test
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX_train = scaler.fit_transform(X_train)
rescaledX_test = scaler.transform(X_test)
```

- dummy variables
```
train = pd.get_dummies(train, columns=['col1', 'col2'], drop_first=True)
```

- Date Time
```
train_date = train["date"].str.split("/", expand=True)
train_date = train_date.rename(columns={0:"month", 1:"day", 2:"year"})
```

6. Fiting model
- logistic for classification
```
# Import LogisticRegression
from sklearn.linear_model import LogisticRegression
# Instantiate a LogisticRegression classifier with default parameter values
logreg = LogisticRegression()

# Fit logreg to the train set
logreg.fit(rescaledX_train, y_train)
```

- regression for quantitative variables
  - consider linear regression assumptions, forward variable selection, transforming data/hist plots
    - https://www.scikit-yb.org/en/latest/api/regressor/residuals.html
```
from sklearn.model_selection import train_test_split
X = train[['col1', 'col2', 'col3']]
y = train[['pred']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20, random_state=40)
```

7. Make predictions and evalute preformance
- for logistic regression, do a confusion matrix
  - want high numbers on diagonals
```
reg.score(X_test)
```
8. Find best performing model
- cross validation
```
from sklearn.model_selection import cross_val_score 

cv_scores3 = cross_val_score(reg, X, y, cv=3)
print(cv_scores3) # looks consistent
```

- Ridge/Lasso to pick better variables 
```
# for specific alpha
from sklearn.linear_model import Lasso

lasso = Lasso(alpha = 0.4, normalize=True)
lasso_coef = lasso.fit(X, y).coef_ # look at which vars are shrunk to 0
```

```
CV to find best alpha
from sklearn.linear_model import LassoCV
lasso = LassoCV(alphas=None, cv=5, random_state=40, normalize=True, max_iter=10000)
lasso.fit(X_train, y_train)

pd.Series(lasso.coef_, index=X_train.columns)

lasso.score(X_test, y_test)
lasso.alpha_
```

- Grid search to tune hyper parameters, pick the best lambda
```
# Import GridSearchCV
from sklearn.model_selection import GridSearchCV
# Define the grid of values for tol and max_iter
tol = [0.01, 0.001, 0.0001]
max_iter = [100, 150, 200]

# Create a dictionary where tol and max_iter are keys and the lists of their values are corresponding values
param_grid = dict(tol=tol, max_iter=max_iter)
```
```
# Instantiate GridSearchCV with the required parameters
grid_model = GridSearchCV(estimator=logreg, param_grid=param_grid, cv=5)

# Use scaler to rescale X and assign it to rescaledX
rescaledX = scaler.fit_transform(X)

# Fit data to grid_model
grid_model_result = grid_model.fit(rescaledX, y)

# Summarize results
best_score, best_params = grid_model_result.best_score_, grid_model_result.best_params_
print("Best: %f using %s" % (best_score, best_params))
```
