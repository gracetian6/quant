### Data Types

- `df.dtypes()`
- `numeric_df = df.select_dtypes(include=['int','float'])`
- `df.columns`

### Uncommon Categories
```
countries = so_survey_df['Country']
country_counts = countries.value_counts()

# Create a mask for only categories that occur less than 10 times
mask = countries.isin(country_counts[country_counts < 10].index)

# Label all other categories as Other
countries[mask] = 'Other'
```
### Get Dummies 
`one_hot_encoded = pd.get_dummies(so_survey_df, columns=['Country'], drop_first=True, prefix='OH')`

### Binarizing Cols
```
so_survey_df['Paid_Job'] = 0

# Replace all the Paid_Job values where ConvertedSalary is > 0
so_survey_df.loc[so_survey_df['ConvertedSalary'] > 0, 'Paid_Job'] = 1
print(so_survey_df[['Paid_Job', 'ConvertedSalary']].head())
```

## Missing Values
- drop all rows with >=1 missing values: `df.dropna(how=‘any’)` 
- drop rows with na values in col: `df.dropna(subset=[‘VersionControl’])` 
- filling na: `df[‘VersionControl’].fillna(value=‘None Given’, inplace=True)`
- dropping cols: `df.drop(columns=[‘ConvertedSalary’])`
- NOTE: values calculated on the train test should be applied to both train and test.

### Stray Characters
```
Replacing stray characters and converting to float:
so_survey_df['RawSalary'] = so_survey_df['RawSalary']\
                              .str.replace(',', '')\
                              .str.replace('$', '')\
                              .str.replace('£', '')\
                              .astype('float')
```                   

To search for other stray characters to replace:
```
# Attempt to convert the column to numeric values
numeric_vals = pd.to_numeric(so_survey_df['RawSalary'], errors='coerce')

# Find the indexes of missing values
idx = numeric_vals.isna()

# Print the relevant rows
print(so_survey_df['RawSalary'][idx])
```
## Standardizing Values

### Visualize Dist
histogram:
`so_numeric_df.hist()` `plt.show()`
boxplot:
`so_numeric_df[['Age', 'Years Experience']].boxplot()` `plt.show()`
- don't forget double brackets

### Min Max Scaling
```
# Import MinMaxScaler
from sklearn.preprocessing import MinMaxScaler

# Instantiate MinMaxScaler
MM_scaler = MinMaxScaler()

# Fit MM_scaler to the data
MM_scaler.fit(so_numeric_df[['Age']])

# Transform the data using the fitted scaler
so_numeric_df['Age_MM'] = MM_scaler.transform(so_numeric_df[['Age']])

# Compare the origional and transformed column
print(so_numeric_df[['Age_MM', 'Age']].head())
```
### Normalization
```
from sklearn.preprocessing import StandardScaler 

SS_scaler = StandardScaler()
SS_scaler.fit(so_numeric_df[['Age']])
so_numeric_df['Age_SS'] = SS_scaler.transform(so_numeric_df[['Age']])

# Compare the origional and transformed column
print(so_numeric_df[['Age_SS', 'Age']].head())
```
### Log transform
```
from sklearn.preprocessing import PowerTransformer

pow_trans = PowerTransformer()
pow_trans.fit(so_numeric_df[['ConvertedSalary']])
so_numeric_df['ConvertedSalary_LG'] = pow_trans.transform(so_numeric_df[['ConvertedSalary']])

# Plot the data before and after the transformation
so_numeric_df[['ConvertedSalary', 'ConvertedSalary_LG']].hist()
plt.show()
```

### Statistical Outlier Removal
```
# Find the mean and standard dev
std = so_numeric_df['ConvertedSalary'].std()
mean = so_numeric_df['ConvertedSalary'].mean()

# Calculate the cutoff
cut_off = std * 3
lower, upper = mean - cut_off, mean + cut_off

# Trim the outliers
trimmed_df = so_numeric_df[(so_numeric_df['ConvertedSalary'] < upper) \
                           & (so_numeric_df['ConvertedSalary'] > lower)]

# The trimmed box plot
trimmed_df[['ConvertedSalary']].boxplot()
plt.show()
```
