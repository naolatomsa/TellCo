from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

db_uri = os.getenv("DATABASE_URL")

def normalize_metrics(engagement_metrics, table_name_centroids):
    # Normalize metrics
    scaler = MinMaxScaler()
    normalized_metrics = scaler.fit_transform(engagement_metrics[['Session Frequency', 'Total Session Duration', 'Total Traffic']])

    # Apply k-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    engagement_metrics['Cluster'] = kmeans.fit_predict(normalized_metrics)
    
    engine = create_engine(db_uri)

    # Convert centroids to a DataFrame for export
    centroids_df = pd.DataFrame(
        kmeans.cluster_centers_, 
        columns=['Session Frequency', 'Total Session Duration', 'Total Traffic']
    )
    centroids_df['Cluster_Index'] = range(len(kmeans.cluster_centers_))

    # Export centroids to database
    centroids_df.to_sql(
        table_name_centroids, engine, if_exists='replace', index=False
    )

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
    
    normalized_metrics=     (engagement_metrics, 'engagement_centroids')
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
    st.pyplot(plt)
