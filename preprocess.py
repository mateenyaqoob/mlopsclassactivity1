import pandas as pd
from sklearn.datasets import load_iris

def preprocess():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df.to_csv("cleaned_iris.csv", index=False)
    print("Data preprocessing completed! Saved to cleaned_iris.csv")

if __name__ == "__main__":
    preprocess()
