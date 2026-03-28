import pandas as pd
import sys
from sklearn.cluster import KMeans

print("Clustering started...")

# Load preprocessed dataset
dataset_path = sys.argv[1]
data = pd.read_csv(dataset_path)

# Select subset of features for clustering
features = ["Income", "Recency", "Age", "Total_Spending"]
available_features = [col for col in features if col in data.columns]

cluster_data = data[available_features].copy()

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data["Cluster"] = kmeans.fit_predict(cluster_data)

# Count samples per cluster
cluster_counts = data["Cluster"].value_counts().sort_index()

with open("clusters.txt", "w", encoding="utf-8") as f:
    for cluster_id, count in cluster_counts.items():
        f.write(f"Cluster {cluster_id}: {count} samples\n")

print("Clustering completed. Saved as clusters.txt")