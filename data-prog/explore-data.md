##  Exploring Data in Python

- data.head()
- data.shape
-data.describe()
- data.columns
- data['column'].value_counts()


## Cleaning / Validating
- `nsfg['nbrnaliv'].replace(8, np.nan, inplace=True)`
- `data.dropna()`
- mean imputation: `data.fillna(data.mean(), inplace=True)`


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

### Comparing CDF
```
# Evaluate the model CDF
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs)

# Plot the model CDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Create and plot the Cdf of log_income
Cdf(log_income).plot()
    
# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('CDF')
plt.show()
```

### Plotting PMF
- use empircaldist library
```
# Extract age
age = brfss['AGE']

# Plot the PMF
Pmf(age).bar()

# Label the axes

plt.xlabel('Age in years')
plt.ylabel('PMF')
plt.show()
```

## Scatterplot with Jitter
```
# Select the first 1000 respondents
brfss = brfss[:1000]

# Add jittering to age
age = brfss['AGE'] + np.random.normal(0, 2.5, size=len(brfss))
# Extract weight
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', markersize=5, alpha=0.2)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')
plt.show()
```

## Box Plot
```
# Drop rows with missing data
data = brfss.dropna(subset=['_HTMG10', 'WTKG3'])

# Make a box plot
sns.boxplot(x='_HTMG10', y='WTKG3', whis=10, data=data)

# Plot the y-axis on a log scale
plt.yscale('log')

# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Height in cm')
plt.ylabel('Weight in kg')
plt.show()
```


## Regression
```
from scipy.stats import linregress
res = linregress(xs, ys)
```
```
# Plot the scatter plot
plt.clf()
x_jitter = xs + np.random.normal(0, 0.15, len(xs))
plt.plot(x_jitter, ys, 'o', alpha=0.2)

# Plot the line of best fit
fx = np.array([xs.min(), xs.max()])
fy = res.intercept + res.slope * fx
plt.plot(fx, fy, '-', alpha=0.7)

plt.xlabel('Income code')
plt.ylabel('Vegetable servings per day')
plt.ylim([0, 6])
plt.show()
```

### Multiple Regression
```
import statsmodels.formula.api as smf
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()
results.params
```

### Predictions
```
# Make the DataFrame
df = pd.DataFrame()
df['educ'] = np.linspace(0, 20)
df['age'] = 30
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2

# Generate and plot the predictions
pred = results.predict(df)
print(pred.head())
```

### Logistic Regression
- `results = smf.logit(...).fit()`
- positive params => more likely, negative params => less likely
