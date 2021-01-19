## Join functions
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

## Merge Ordered Data
- `merge_ordered()` and `merge_asof()`
## Query to Filter
- sql queries in python
- `stocks.query('nike > 90 and disney < 140')` 
- `gdp_pivot.query('date >= "1991-01-01"')`

## Pivot Tables 
```
# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')
```

Unpivot table
```
# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars=['year'], var_name='month', value_name='unempl_rate')
```
