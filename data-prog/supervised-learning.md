## Supervised Learning

### Train Test Split
```
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = 
  train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)
```

### Regression
See also `explore-data.md`:
```
import numpy as np
from sklearn.linear_model import LinearRegression

# Create the regressor: reg
reg = LinearRegression()

# Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1,1)

# Fit the model to the data
reg.fit(X_fertility, y)

# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)

# Print R^2 
print(reg.score(X_fertility, y))

# Plot regression line
plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.show()
```

### Cross Validation
```
from sklearn.model_selection import cross_val_score

# Perform 3-fold CV
cvscores_3 = cross_val_score(reg, X, y, cv=3)
print(np.mean(cvscores_3))
```
