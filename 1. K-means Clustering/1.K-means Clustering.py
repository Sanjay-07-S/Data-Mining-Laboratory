import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


def load_and_preprocess_data(filename='your_dataset.csv'):

    data = pd.read_csv(filename)


    label_encoders = {}
    for column in data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

    X = data.drop('Target', axis=1)
    y = data['Target']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y


def fit_and_plot_kmeans(X, k):

    kmeans = KMeans(n_clusters=k, random_state=0)
    labels = kmeans.fit_predict(X)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)


    plt.figure(figsize=(10, 7))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', marker='o', s=50)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=200, marker='x',
                label='Centroids')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('K-Means Clustering Results')
    plt.legend()
    plt.show()


if __name__ == "__main__":

    X, y = load_and_preprocess_data('original_1.csv')
    k = int(input("Enter the number of clusters (k): "))

    fit_and_plot_kmeans(X, k)
