"""
1. Write a function to calculate all possible assignment vectors of 2n users,
where n users are assigned to group 0 (control) and n users are assigned to
group 1 (treatment).
"""

def backtrack(n, combo="", num0=0):
    if len(combo) == 2 * n:
        soln.append(combo)
    else:
        if num0 < n:
            backtrack(n, combo+"0", num0+1)

        num1 = len(combo) - num0
        if num1 < n:
            backtrack(n, combo+"1", num0)

soln = []
backtrack(3)
print(soln)
print(len(soln))
