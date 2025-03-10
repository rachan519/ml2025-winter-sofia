import numpy as np
from sklearn.metrics import precision_score, recall_score

N = int(input("Enter the number of points (N): "))

x = np.zeros(N, dtype=int)
y = np.zeros(N, dtype=int)

for i in range(N):
    print(f"\nPoint {i+1}:")
    x[i] = int(input("Enter x value (0 or 1): "))
    y[i] = int(input("Enter y value (0 or 1): "))

# Compute precision and recall using scikit-learn
precision = precision_score(x, y, zero_division=1)
recall = recall_score(x, y, zero_division=1)

print(f"\nPrecision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
