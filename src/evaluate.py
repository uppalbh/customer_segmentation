from sklearn.metrics import silhouette_score

def evaluate_model(model, X):
    labels = model.labels_
    score = silhouette_score(X, labels)
    return score

def cluster_summary(df):
    return df.groupby("Cluster").mean()
