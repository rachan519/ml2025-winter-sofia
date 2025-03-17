import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def get_input_pairs(count, label):
    """Reads count number of (x, y) pairs from user input."""
    data = np.zeros((count, 2))
    print(f"Enter {count} (x, y) pairs for {label} set:")
    for i in range(count):
        x = float(input(f"Enter x for pair {i + 1}: "))
        y = int(input(f"Enter y for pair {i + 1}: "))
        data[i] = [x, y]
    return data

def main():
    # Read training data
    N = int(input("Enter the number of training samples (N): "))
    TrainS = get_input_pairs(N, "training")
    
    # Read test data
    M = int(input("Enter the number of test samples (M): "))
    TestS = get_input_pairs(M, "test")
    
    # Extract features and labels
    X_train, y_train = TrainS[:, 0].reshape(-1, 1), TrainS[:, 1]
    X_test, y_test = TestS[:, 0].reshape(-1, 1), TestS[:, 1]
    
    best_k = 1
    best_accuracy = 0.0
    
    # Try different values of k
    for k in range(1, 11):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        
        print(f"Accuracy for k={k}: {acc:.4f}")
        
        if acc > best_accuracy:
            best_accuracy = acc
            best_k = k
    
    print(f"Best k: {best_k}, Test Accuracy: {best_accuracy:.4f}")

if __name__ == "__main__":
    main()
