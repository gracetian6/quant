# 120 Data Science Questions: Probability

## Amoeba 

Example 2.7.2 (Branching process). A single amoeba, Bobo, lives in a pond. After
one minute Bobo will either die, split into two amoebas, or stay the same, with equal
probability, and in subsequent minutes all living amoebas will behave the same way,
independently. What is the probability that the amoeba population will eventually
die out?

### Amoeba Solution (Conditioning)
Let D be the event that the population eventually dies out; we want to and P(D).
Let B_0, B_1, B_2 correspond to the event that Bobo will either die, split into two amoebas, or stay the same, with equal
probability. 

P(D) = 1/4P(D|B_0) + 1/4P(D|B_1) + 1/2P(D|B_2) = 1/4 * 1 + 1/4*P(D) + 1/2P(D)^2

- P(D|B_1) = P(D) since we're back to where we started. 
- P(D|B_2) = P(D)^2 since both amoeba need to die for P(D|B_2)

### Universality of Uniform
Given draws from a normal distribution with known parameters, how can you simulate draws from a uniform distribution?

- plug in Z/the draws above into its normal CDF 
- in general plugging in the value to the CDF of the same random variable

## Geometric / First Success Dist 
X ~ Geom(p); X is the number of **failures that we will achieve before we achieve our first success**. 
- Our successes have probability p. E(X) = 1/p - 1.

X ~ FS(p); X is the number of **failures that we will achieve including our first success**. 
- Our successes have probability p. E(X) = 1/p.

- Ex: You have a group of couples that decide to have children until they have their first girl, after which they stop having children. What is the expected gender ratio of the children that are born? What is the expected number of children each couple will have?
  - gender ratio is 1:1, expect number of children is 2.
  - Let X be the number of children until getting a female (happens with prob 1/2). This follows a first success distribution with probability 1/2

