## Does Linear Regression Reverse have inverse?

If we have linear regression of y on x and the same of x on y, is the coefficient differ by an inverse?

### Soln
No, it doesn't because the linear regression of y on x minimizes the _vertical errors_, while that on x on y minimizes the _horizontal errors_.
These are 2 different objectives, so the coefficient won't be an inverse of each other.

## Finding intercept using only slope function
Let x be a _nxp_ vector and y be a _nx1_ vector. We have a function f(x, y) that takes finds the slope beta of y on x with no intercept. 

How can we use this to find the intercept?

### Soln
Add column of 1s to x. Plug it into the function. The value that corresponds to the 1s would be the intercept.

## Heavy tailed distributions

Can you tell me some symmetric, heavy tailed distributions? Anything more heavy tailed than normal will work.

### Soln
t distribution is heavier at the ends.
Cauchy distribution is also heavier. (ratio of two normal distributions)

## Joint Uniform Distribution on Unit Disk
