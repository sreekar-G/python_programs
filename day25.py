#Every ML model uses randomness:
#
#1. Weight initialisation  → random starting point
#2. Train/test split       → randomly split data
#3. Mini-batch selection   → randomly pick samples
#4. Dropout                → randomly ignore neurons
#5. Data augmentation      → randomly transform images

#Most Important Topic

# This is what sklearn does internally!
#data = np.arange(10)         # [0,1,2,3,4,5,6,7,8,9]

#np.random.seed(42)
#np.random.shuffle(data)      # shuffle first!
# → [6, 1, 4, 9, 2, 7, 3, 0, 5, 8]

#split = int(0.8 * len(data)) # 80% train

#train = data[:split]         # → [6,1,4,9,2,7,3,0]
#test  = data[split:]         # → [5, 8]

#1. np.random.seed() — Reproducibility
#2. np.random.randint() — Random Integers
#3. np.random.normal() — Bell Curve Numbers
#4. np.random.shuffle() vs np.random.choice()


import numpy as np 

if __name__ == "__main__" :
	np.random.seed(42)
	
	random_matrix  = np.random.normal(0, 1, (100, 3))
	print(f"Task 1: Dataset shape → {np.shape(random_matrix)}")
	

	#y = 2*X[:,0] + 3*X[:,1] - X[:,2] + noise
	noise = np.random.normal(0, 0.5, 100)
	y = 2 * random_matrix[:,0] + 3 * random_matrix[:,1] - random_matrix[:,2] + noise
	print(f"Task 2: First 5 target values → {y[:5]}")

	indices = np.arange(len(random_matrix))	
	np.random.shuffle(indices)	

	split = int(0.8 * len(random_matrix))
	
	train_data = random_matrix[indices][:split]
	test_data = random_matrix[indices][split:]
	train_y = y[indices][:split]
	test_y = y[indices][split:]
	
	print("Task 3:")
	print(f"  Train random_matrix shape → {np.shape(train_data)}")	
	print(f"  Test random_matrix shape  → {np.shape(test_data)}")
	print(f"  Train y shape  → {np.shape(train_y)}")
	print(f"  Test y shape  → {np.shape(test_y)}")
	
	print("Task 4:")
	
	train_data_mean = np.mean(train_data, axis=0)
	train_data_std = np.std(train_data, axis=0)
	scaled_train_data = (train_data - train_data_mean) / train_data_std
	scaled_test_data_with_train = (test_data - train_data_mean) / train_data_std
	print(f"Train mean ≈ {round(np.mean(scaled_train_data), 2)}   std ≈ {round(np.std(scaled_train_data), 3)}  ✅")
	print(f"Train mean ≈ {round(np.mean(scaled_test_data_with_train), 2)}   std ≈ {round(np.std(scaled_test_data_with_train), 3)}  ")
