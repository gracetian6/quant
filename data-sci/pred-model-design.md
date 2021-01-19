## Predictive Modeling Design Questions
### Social Media to Predict Weather
- Twitter, FB, Instagram API
- For example for twitter: features from each tweet (date, #favs, retweets), content multivariate time series model to predict weather

### Feed that shows relevant content 
We want to build a recommendation engine!
- A recommendation engine is a system that suggests products, services, information to users based on analysis of data.

1. show content based on popularity (ex: news articles)
2. content based filtering (if there's enough user usage data)
    - compares user-profile (user likes, movie stars/genres) and item-profile (movie stars/genres) 
    - books with the same author, publisher, genre, pages as book A first, then slowly make it less strict 
3. collaborative filtering (otherwise if there's not enough user usage data)
    - uses _user behavior_ for recommending items (e.g. transaction history, ratings, selection, purchase info)
    - books read by people that have read book A and books with highest count are on top of list 


### Sources
- https://github.com/kojino/120-Data-Science-Interview-Questions/blob/master/predictive-modeling.md
- Recommendation Engine: https://medium.com/voice-tech-podcast/a-simple-way-to-explain-the-recommendation-engine-in-ai-d1a609f59d97
