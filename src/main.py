from models.perceptron import Perceptron

def main():
    # Create a Perceptron instance
    ppn = Perceptron(eta=0.01, n_iter=50)
    # Fit the Perceptron to some training data (X_train, y_train)
    # ppn.fit(X_train, y_train)


if __name__ == "__main__":
    main()