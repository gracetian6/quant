## Exploring Data
- Dropping the `gender` column in chess dataset: `chess.drop(columns="Gender", inplace=True)`
- Setting index: `food = food.set_index('item')`
- Forward filling NA: `data.fillna(method = "ffill")`
- Filling NA with 0: `data.fillna(0)`
- Row Indices: `food.index`
- Boolean Vector of NAs: `data.isna()`

## Transforming Data
- Selecting Columns: `df.loc[:,["gh owner"]]`



## Joining Data 
#### Join Arguments for merge function
- on, left_on, right_on
- how ("left", "right", "inner", 
- suffixes=('_1', '_2')

#### Join Types (Row Merging)
- inner join: only returns connected matching rows
`data1.merge(data2, on="col")`

- left join: returns all connected rows and unconnected rows from left table (nulls in right)
`data1.merge(data2, on="col", how="left")`

- right join: returns all connected rows and unconnected rows from right table (nulls in left)
`data1.merge(data2, on="col", how="right")`

- full join: returns connected rows and unconnected rows from both left and right tables

- outer join
- self merge: ```data.merge(data, ...)``` for hierarchical, sequential graph data etc

## Combine Vertically with .concat()
- Along columns: `pd.concat([df1, df2], axis=0)`
- Along rows: `pd.concat([df, df2], axis=1)`

## Merge Ordered Data
- `merge_ordered()` and `merge_asof()`

## Query to Filter
- sql queries in python
- `stocks.query('nike > 90 and disney < 140')` 
- `gdp_pivot.query('date >= "1991-01-01"')`

## Cleaning Data 
### Pivot Tables 
- Pivot data so that rows are country, columns are year, values are bmi
  - `df.pivot_table(index = "country", columns = "year", values = "bmi")`
- `df.pivot_table(values = 'stars', index = 'language', aggfunc = np.sum)`


Unpivot table
```
# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars=['year'], var_name='month', value_name='unempl_rate')
```
