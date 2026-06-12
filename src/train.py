import pandas as pd
from sklearn.cluster import KMeans
from preprocessing import preprocess

def train_model(path, n_clusters=4):
    df, X, scaler = preprocess(path)

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto")
    model.fit(X)

    df["Cluster"] = model.labels_

    return model, df, scaler

if __name__ == "__main__":
    model, df, scaler = train_model("data.csv")
    print(df["Cluster"].value_counts())
