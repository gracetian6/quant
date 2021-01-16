# 120 Data Science Questions: Probability

## Amoeba 

Example 2.7.2 (Branching process). A single amoeba, Bobo, lives in a pond. After
one minute Bobo will either die, split into two amoebas, or stay the same, with equal
probability, and in subsequent minutes all living amoebas will behave the same way,
independently. What is the probability that the amoeba population will eventually
die out?

### Amoeba Solution
Let D be the event that the population eventually dies out; we want to and P(D).
Let B_0, B_1, B_2 correspond to the event that Bobo will either die, split into two amoebas, or stay the same, with equal
probability. 

P(D) = 1/4P(D|B_0) + 1/4P(D|B_1) + 1/2P(D|B_2) = 1/4 * 1 + 1/4*P(D) + 1/2P(D)^2

- P(D|B_1) = P(D) since we're back to where we started. 
- P(D|B_2) = P(D)^2 since both amoeba need to die for P(D|B_2)
