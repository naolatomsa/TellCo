from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def normalize_metrics(engagement_metrics):
    # Normalize metrics
    scaler = MinMaxScaler()
    normalized_metrics = scaler.fit_transform(engagement_metrics[['Session Frequency', 'Total Session Duration', 'Total Traffic']])

    # Apply k-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    engagement_metrics['Cluster'] = kmeans.fit_predict(normalized_metrics)

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

