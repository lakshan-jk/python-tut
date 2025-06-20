import numpy as np


data = [1, 2, 3, 4, 5]

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

print("Range:", max(data) - min(data))
print("IQR:", np.percentile(data, 75) - np.percentile(data, 25))
