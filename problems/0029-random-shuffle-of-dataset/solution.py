import numpy as np

def shuffle_data(X, y, seed=42):
	# Your code here
	rng = np.random.seed(seed=seed)

	n = X.shape[0]
	ind = np.random.choice(np.arange(n), size=n, replace=False)
	return X[ind], y[ind]