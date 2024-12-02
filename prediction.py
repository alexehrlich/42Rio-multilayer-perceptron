from network import Network, Layer
import pandas as pd
import math
import numpy as np
from functions import binary_cross_entropy
from exceptions import *

try:
	net = Network.load_model("model.pkl")
except Exception as e:
	print("Error:", e.message)
	exit()

try:
	features_df_test = pd.read_csv("./csv/created/features_test.csv")
	target_df_test = pd.read_csv("./csv/created/target_test.csv")
except Exception as e:
	print("Error:", str(e))
	print("Run <make preprocess_data> first.")
	exit()

X_test = features_df_test.to_numpy()
Y_test = target_df_test.to_numpy()

results = []
BCE_losses = []
total = len(X_test)
right = 0
wrong = 0
sample = 0
for test, target in zip(X_test, Y_test):
	sample += 1
	test_c = test.reshape(-1, 1)
	out = net.feed_forward(test_c)
	results.append(out)
	bce = binary_cross_entropy(target, out)
	BCE_losses.append(bce)
	print(f"Sample {sample}")
	print(f"Label: {target[0]}")
	print(f"Confidence for class 0: {out[0][0]*100:.1f}%")
	print(f"Confidence for class 1: {out[1][0]*100:.1f}%")
	print(f"Binary Cross Entropy loss: {bce}\n")
	if out[0] > out [1]:
		result = 0
	else:
		result = 1
	if target[0] == result:
		right += 1
	else:
		wrong += 1
print(f"Number of test samples: {total}")
print(f"Incorrect classifications: {wrong}, {(wrong/total*100):.2f}%")
print(f"Correct classifications: {right}, {(right/total*100):.2f}%")
print(f"Avergae BCE loss: {np.mean(BCE_losses)}")


