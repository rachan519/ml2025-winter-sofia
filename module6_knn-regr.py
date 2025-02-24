import numpy as np

class KNNRegression:
    def __init__(self, k, X_train, y_train):
        self.k = k
        self.X_train = X_train
        self.y_train = y_train
    
    def predict(self, X_query):
        if k > N:
            print("Error: k cannot be greater than N")
            exit()
            
        distances = np.abs(self.X_train - X_query)
        
        nearest_indices = np.argsort(distances)[:self.k]

        return np.mean(self.y_train[nearest_indices])

N = int(input("Enter the number of data points (N): "))
k = int(input("Enter the number of nearest neighbors (k): "))


X_train = np.zeros(N)
y_train = np.zeros(N)

for i in range(N):
    x = float(input(f"Enter x value for point {i+1}: "))
    y = float(input(f"Enter y value for point {i+1}: "))
    X_train[i] = x
    y_train[i] = y

X_query = float(input("Enter the X value to predict Y: "))

knn = KNNRegression(k, X_train, y_train)
Y_pred = knn.predict(X_query)

print(f"Predicted Y value: {Y_pred}")
