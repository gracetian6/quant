## 120 Data Science Questions: Programming
Github Folder for programming questions in 120 Data Science Questions.
Coded in R and Python.

### R Troubleshooting 
You should not define a global variable and expect to get it modified within the function. 
R's paradigm is to be "pass by value". Otherwise, return df/variable to get it modified.

```{r}
c = 1
test <- function(){c = 2}
test()
print(c) # prints 1
```

## Sources
- https://stackoverflow.com/questions/8419877/modify-variable-within-r-function
