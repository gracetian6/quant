## INNER join
- only returns connected matching rows
`data1.merge(data2, on="col")`

## LEFT join
- returns all connected rows and unconnected rows from left table (nulls in right)
`data1.merge(data2, on="col", how="left")`

## RIGHT join
- returns all connected rows and unconnected rows from right table (nulls in left)
`data1.merge(data2, on="col", how="right")`

## FULL join
- returns connected rows and unconnected rows from both left and right tables

## OUTER join

## self merge
```data.merge(data, ...)```
for hierarchical, sequential graph data etc

##ARGUMENTS
- on, left_on, right_on
- how ("left", "right", "inner", 
- suffixes=('_1', '_2')
