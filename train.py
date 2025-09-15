import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

def train():
    # Load cleaned data
    df = pd.read_csv("cleaned_iris.csv")
    X, y = df.iloc[:, :-1], df['target']

    # Train logistic regression
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    # Save model
    joblib.dump(model, "model.pkl")
    print("Model training completed! Saved to model.pkl")

if __name__ == "__main__":
    train()
