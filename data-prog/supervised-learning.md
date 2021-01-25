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

reg = LinearRegression()
reg.fit(X_rooms, y)
```
