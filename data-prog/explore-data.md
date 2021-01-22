##  Exploring Data in Python

- data.head()
- data.shape
-data.describe()
- data.columns
- data['column'].value_counts()


## Cleaning / Validating
- `nsfg['nbrnaliv'].replace(8, np.nan, inplace=True)`
- `data.dropna()`

## Filtering
- `preterm_weight = birth_weight[preterm]
  - opposite is `birth_weight[~preterm]`
  
## Visualization 
``` 
import matplot.pyplot as plt
plt.hist(agecon, bins=20)
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnances')
plt.show()
```

### Normal CDF
```
from scipy.stats import norm
xs = np.linspace(-3, 3)
ys = norm(0, 1).cdf(xs)
plt.plot(xs, ys, color='gray')
```
