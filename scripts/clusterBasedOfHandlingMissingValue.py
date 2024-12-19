from sklearn.cluster import KMeans
import pandas as pd

def handle_missing_value_cluster(data, column_name, n_clusters=3):
    # Step 1: Apply KMeans clustering to the data (before imputation)
    # For simplicity, we apply clustering on the 'Avg RTT UL (ms)' column, but you can include more features if needed.
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)

    # Fill missing values temporarily with the mean to avoid errors in clustering
    data[column_name] = data[column_name].fillna(data[column_name].mean())
    
    # Fit KMeans and predict clusters
    data['Cluster'] = kmeans.fit_predict(data[[column_name]])
    
    # Step 2: For each cluster, calculate the mean or median (you can use median if preferred)
    cluster_means = data.groupby('Cluster')[column_name].mean()

    # Step 3: Impute missing values within each cluster using the mean of the cluster
    for cluster in data['Cluster'].unique():
        cluster_mean = cluster_means[cluster]
        data.loc[(data['Cluster'] == cluster) & (data[column_name].isnull()), column_name] = cluster_mean
    
    return data
