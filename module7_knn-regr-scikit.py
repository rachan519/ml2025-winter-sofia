import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNRegressionModel:
    def __init__(self):
        self.N = 0  
        self.k = 0 
        self.X_train = None
        self.y_train = None
        self.model = None

    def get_positive_integer_input(self, prompt):
        """Get a positive integer from the user."""
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    print("Please enter a positive integer.")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def get_float_input(self, prompt):
        """Get a float value from the user."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a real number.")

    def collect_data(self):
        """Collect N data points from the user."""
        self.N = self.get_positive_integer_input("Enter the number of points (N): ")
        self.k = self.get_positive_integer_input(f"Enter the number of neighbors (k ≤ {self.N}): ")

        while self.k > self.N:
            print(f"Error: k ({self.k}) cannot be greater than N ({self.N}).")
            self.k = self.get_positive_integer_input(f"Enter a valid number of neighbors (k ≤ {self.N}): ")

        self.X_train = np.zeros(self.N)
        self.y_train = np.zeros(self.N)

        print(f"\nEnter {self.N} points (x, y) one by one:")
        for i in range(self.N):
            print(f"Point {i+1}:")
            self.X_train[i] = self.get_float_input(" Enter x value: ")
            self.y_train[i] = self.get_float_input(" Enter y value: ")

        self.X_train = self.X_train.reshape(-1, 1)

    def train_model(self):
        """Train the k-NN regressor model."""
        variance = np.var(self.y_train)

        if variance == 0:
            print("Warning: All y values are the same. The model may not make meaningful predictions.")

        self.model = KNeighborsRegressor(n_neighbors=self.k)
        self.model.fit(self.X_train, self.y_train)

    def predict(self):
        """Make a prediction based on user input."""
        X_test = self.get_float_input("\nEnter the X value for prediction: ")
        X_test = np.array([[X_test]])  
        y_pred = self.model.predict(X_test)[0]

        print(f"\nResults:")
        print(f"Predicted Y value: {y_pred:.4f}")
        print(f"Variance of training labels: {np.var(self.y_train):.4f}")

    def run(self):
        """Run the complete k-NN regression process."""
        self.collect_data()
        self.train_model()
        self.predict()

if __name__ == "__main__":
    knn_model = KNNRegressionModel()
    knn_model.run()
