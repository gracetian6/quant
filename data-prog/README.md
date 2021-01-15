# 120 Data Science Questions: Programming
Github Folder for programming questions in 120 Data Science Questions.
Coded in R and Python.

## R Troubleshooting 
### Pass By Value
You should not define a global variable and expect to get it modified within the function. 
R's paradigm is to be "pass by value". Otherwise, return df/variable to get it modified.

```{r}
c = 1
test <- function(){c = 2}
test()
print(c) # prints 1
```

**Instead** to modify a variable with a function, you have to reset the variable to the output of the function. For example,
notice the `result` variable in the code below. 

```{r}
n <- 3

backtrack <- function(n, combo=c(), num0=0){
  result <- c()
  if (length(combo) == 2 * n){
    result <- combo
  } else {
    # general case
    if (num0 < n){
      result <- rbind(result,backtrack(n, append(combo, 0), num0+1))
    } 
    num1 = length(combo) - num0
    if (num1 < n){
      result <- rbind(result,backtrack(n, append(combo, 1), num0))
    }
  }
  return(result)
}
result<-backtrack(n)
```

## Sources
- https://stackoverflow.com/questions/8419877/modify-variable-within-r-function
