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


## Multinomial Dist
- Mult_k(n, p)
- n items which can fall into any one of k buckets independent with prob p=(p_1,...,p_k)

Ex: splitting 12 people into 3 teams of 4
- (12!)/(4! 4! 4!) ways
- Multinomial distribution with n=12, k=3 (this is when classes are indistinguishable)

Ex: 100 students sorted into 4 houses with equal probability
- number ppl in each house ~ Mult_4(100, [1/4, 1/4, 1/4, 1/4])

## Birthday Problem (Hash Collisions)

10. Your hash function assigns each object to a number between 1:10, each with equal probability. With 10 objects, what is the probability of a hash collision? What is the expected number of hash collisions? What is the expected number of hashes that are unused.

- do complementary counting step by step
- Prob of hash collision: 1 - (10!/10^10)
- Prob Bin 1 is empty = (1-1/10)^10 = (9/10)^10
- Expected number of hash collisions: 1-10*(9/10)^10
  - E[empty bins] = 10 * (9/10)^10
    - using linearity of expectation and prob above that bin 1 is empty
    - this is also E[unused hashes]

## Matching Socks / Uber & Lyft
- do it case by case, consider one car at a time.

2 Uber, 3 Lyft. 
What's probability that all lyft arrive first? 
- 3/5 * 2/4 * 1/3

What's probability that all Uber arrive first?
- 2/5 * 1/4 = 1/10

## Drunk Passenger

## Regression to mean
If a sample point of a random variable is extreme (nearly an outlier), a future point will be closer to mean or average on further measurements. 

Ex: Let's say you have a very tall father. On average, what would you expect the height of his son to be? Taller, equal or shorter? What if you had a very short father? 
- Ans: For tall father, Expected height of son is shorter 

TODO find theoretical intutiion
