import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

def plot_elbow(wcss):
    plt.plot(range(1, len(wcss) + 1), wcss)
    plt.title("Elbow Method")
    plt.xlabel("Clusters")
    plt.ylabel("WCSS")
    plt.show()

def plot_clusters_2d(X, labels, centroids=None):
    plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels, cmap="viridis")

    if centroids is not None:
        plt.scatter(
            centroids[:, 0],
            centroids[:, 1],
            s=200,
            c="red",
            marker="X"
        )

    plt.title("Customer Segments")
    plt.show()

def plot_pca(X, labels, model=None):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap="viridis")

    if model is not None:
        centroids = pca.transform(model.cluster_centers_)
        plt.scatter(centroids[:, 0], centroids[:, 1], c="red", s=200, marker="X")

    plt.title("PCA Cluster Visualization")
    plt.show()
