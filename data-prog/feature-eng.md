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
