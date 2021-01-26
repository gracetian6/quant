# Neural Networks
AI > ML > Deep Learning
- Classical models use one algorithm for feature extraction followed by a machine learning classifier
- neural networks do the optimization altogether.
- first few layers transform the input into features which are easy to be classified
- final layer separates the data based on the features which the previous layers have generated


## Back Propagation
- starts with last parameter, and works its way backwards to estimate all other parameters

## Activation Function
Activation functions are non-linear functions which are inserted in each layer of the neural network, making neural networks nonlinear and allowing them to deal with highly non-linear datasets, thus making them much more powerful.
- ReLu(x) = max(0, x); `nn.ReLU()`

## Loss function
- measures how well the model is doing
- regression: least squared loss
- classification: softmax cross-entropy loss
  - P(Y=k|X = x_i) = e^sk / \sum_j {e^s j}
  - turns numbers into probabilites 
- 
