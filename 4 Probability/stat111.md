## Does Linear Regression Reverse have inverse?

If we have linear regression of y on x and the same of x on y, is the coefficient differ by an inverse?

### Soln
No, it doesn't because the linear regression of y on x minimizes the _vertical errors_, while that on x on y minimizes the _horizontal errors_.
These are 2 different objectives, so the coefficient won't be an inverse of each other.

## Finding intercept using only slope function
Let x be a _nxp_ vector and y be a _nx1_ vector. We have a function f(x, y) that takes finds the slope beta of y on x with no intercept. 

How can we use this to find the intercept?

### Soln
Add column of 1s to x. Plug it into the function. The function value that corresponds to the 1s would be the intercept.

Do out an example with x as a 2x2 matrix and y as a 2x1 matrix.
Once you add the 1s column to x, then you would get an intercept when you expand out the equations.

## Heavy tailed distributions

Can you tell me some symmetric, heavy tailed distributions? Anything more heavy tailed than normal will work.

### Soln
t distribution is heavier at the ends.
Cauchy distribution is also heavier. (ratio of 2 normal distributions)

## Joint Uniform Distribution on Unit Disk
Let F(x, y) be a joint distribution that is unifomr on the unit disk. 
What is the correlation between x and y? Are x and y independent?

### Soln
No, x and y have **0 correlation**. Intuitively, its because everything is symmetric. For every positive value (x, y) there is a negative value (x, y) equally.

As a proof, Cov(X, Y) = E(XY) - E(X)E(Y) = 0 - 0 * 0 = 0

No, x and y are not independent. We can tell by looking at the pdf.

f(x, y) = 1/pi within circle, and 0 otherwise. This is because its uniform, so pdf is 1/Area.
If x and y are independent, then f(x, y) = f(x)f(y). So f(x) = f(y) = 1/sqrt(pi).

We know this is not possible because pdf would not integrate to 1. Also because if you look at 
vertical and horizontal slices of uniform circle, we know that pdf of x isn't constant. 

## Covariance Matrix
What is the covariance matrix?

How would you find the find the covariance matrix of a matrix X?

### Soln
Covariance matrix is a sq matrix that gives the covariance between each pair of elements.

You can calculate covariance matrix by doing:
E(X X^T) - E(X)E(X^T)


## Tips
- for matrices, you need to write it out.

## X, Y, Z iid U(0,1). Prob X+Y>Z?

Pyramid of cube with points (1,0,1), (0,1,1) and (0,0,0) since X + Y = Z. We take region below the plane since <Z. 
The region above is a pyramid of base 1/2 and height 1 => volume is 1/3 * 1/2 * 1 = 1/6.
Region below is 1-1/6 = 5/6
