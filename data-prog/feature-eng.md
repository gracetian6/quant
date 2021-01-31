### Data Types

- `df.dtypes()`
- `numeric_df = df.select_dtypes(include=['int','float'])`
- `df.columns`

### Uncommon Categories
```
# Create a series out of the Country column
countries = so_survey_df['Country']

# Get the counts of each category
country_counts = countries.value_counts()

# Create a mask for only categories that occur less than 10 times
mask = countries.isin(country_counts[country_counts < 10].index)

# Label all other categories as Other
countries[mask] = 'Other'
```
