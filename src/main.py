from models.perceptron import Perceptron
from dataset_loader import Dataset

def main():
    # Load the dataset
    SAMPLE_IRIS_DATASET = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

    dataset = Dataset.load_dataset(SAMPLE_IRIS_DATASET)
    ppn = Perceptron(eta=0.01, n_iter=50)



if __name__ == "__main__":
    main()