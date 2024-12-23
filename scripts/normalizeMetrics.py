from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def normalize_metrics(engagement_metrics):
    # Normalize metrics
    scaler = MinMaxScaler()
    normalized_metrics = scaler.fit_transform(engagement_metrics[['Session Frequency', 'Total Session Duration', 'Total Traffic']])

    # Apply k-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    engagement_metrics['Cluster'] = kmeans.fit_predict(normalized_metrics)
    
    np.savetxt('engagement_centroids.csv', kmeans.cluster_centers_, delimiter=',')

    # Create a DataFrame for visualization
    normalized_metrics_df = pd.DataFrame(
        normalized_metrics, 
        columns=['Session Frequency', 'Total Session Duration', 'Total Traffic']
    )
    normalized_metrics_df['Cluster'] = engagement_metrics['Cluster'].astype(str)

    # Visualize clusters
    sns.pairplot(data=normalized_metrics_df, hue='Cluster', palette='viridis')
    plt.show()

    return normalized_metrics

def optimize_k_in_k_means_clustering(engagement_metrics):
    
    normalized_metrics= normalize_metrics(engagement_metrics)
    inertia = []
    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(normalized_metrics)
        inertia.append(kmeans.inertia_)

    # Plot the elbow curve
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 10), inertia, marker='o')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.show()

