import numpy as np

#Elementwise comparison with 0. Returns always the max of the elementwise
#comparison. For negative ones 0, else the the element.
def ReLU(input):
	return np.maximum(input, 0)

def derivative_ReLU(input):
	return np.where(input > 0, 1, 0)

def sigmoid(z):
	return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
	return sigmoid(z)*(1-sigmoid(z))

#Gets a vector and returns a vector
def softmax(input):
	temp = np.exp(input - np.max(input))
	return temp / np.sum(temp)

def categorial_cross_entropy_loss(predictions, targets):
	# Ensure numerical stability by adding epsilon
	epsilon = 1e-15
	predictions = np.clip(predictions, epsilon, 1 - epsilon)

	# Calculate the log of predictions
	log_predictions = np.log(predictions)

	# Element-wise multiplication of log_predictions and targets
	temp = np.multiply(log_predictions, targets)

	# Calculate the cross-entropy loss
	loss = -np.sum(temp)

	return loss

def derivative_crossentropy_softmax(layer_out, target_vec):
	return layer_out - target_vec

def binary_cross_entropy(y_true, y_pred):
	epsilon = 1e-15
	y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  # Avoid log(0)
	return - (y_true * np.log(y_pred[1]) + (1 - y_true) * np.log(y_pred[0]))

func_deriv = {
	None: None,
	ReLU: derivative_ReLU,
	sigmoid: sigmoid_prime,
	softmax: None
}

def he_initialization(layer, prev_layer_nodes):
	np.random.seed(39)
	layer.weights = np.random.randn(layer.nodes, prev_layer_nodes) * np.sqrt(2 / prev_layer_nodes)

def xavier_initialization(layer, prev_layer_nodes):
	np.random.seed(39)
	limit = np.sqrt(6 / (layer.nodes + prev_layer_nodes))
	layer.weights = np.random.uniform(-limit, limit, size=(layer.nodes, prev_layer_nodes))