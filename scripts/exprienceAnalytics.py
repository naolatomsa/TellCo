import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine


def agggregate_metrics_per_customer(data, table_name, db_uri):
    aggregated = data.groupby('MSISDN/Number').agg({
        'Avg RTT DL (ms)': 'mean',
        'Avg RTT UL (ms)': 'mean',
        'TCP DL Retrans. Vol (Bytes)': 'mean',
        'TCP UL Retrans. Vol (Bytes)': 'mean',
        'Avg Bearer TP DL (kbps)': 'mean',
        'Avg Bearer TP UL (kbps)': 'mean',
        'Handset Type': 'first'
    }).reset_index()

    # Calculate composite metrics
    aggregated['Avg_RTT'] = (aggregated['Avg RTT DL (ms)'] + aggregated['Avg RTT UL (ms)']) / 2
    aggregated['Avg_Throughput'] = (aggregated['Avg Bearer TP DL (kbps)'] + aggregated['Avg Bearer TP UL (kbps)']) / 2
    aggregated['Avg_TCP_Retransmission'] = (aggregated['TCP DL Retrans. Vol (Bytes)'] + aggregated['TCP UL Retrans. Vol (Bytes)']) / 2


    # Keep only relevant columns
    aggregated = aggregated[['MSISDN/Number', 'Avg_TCP_Retransmission', 'Avg_RTT', 'Avg_Throughput', 'Handset Type']]
    
     # Save the file in the current directory
    # aggregated.to_csv('experience_metrics.csv', index=False)
    # print(f"Aggregated metrics saved to {'experience_metrics.csv'}")
    engine = create_engine(db_uri)

    aggregated.to_sql(
        table_name, engine, if_exists='replace', index=False
    )
    return aggregated;




# Task 3.2: Compute Top, Bottom, and Most Frequent
# Top 10, Bottom 10, Most Frequent
import pandas as pd

def most_frequent(aggregated):
    metrics = ['Avg_TCP_Retransmission', 'Avg_RTT', 'Avg_Throughput']
    results = []

    for metric in metrics:
        top_10 = aggregated.nlargest(10, metric)[metric].values
        bottom_10 = aggregated.nsmallest(10, metric)[metric].values
        most_frequent = aggregated[metric].mode()[0]

        results.append({
            'Metric': metric,
            'Top 10': ', '.join(map(str, top_10)),
            'Bottom 10': ', '.join(map(str, bottom_10)),
            'Most Frequent': most_frequent
        })

    # Convert results to a DataFrame
    results_df = pd.DataFrame(results)
    return results_df


# Task 3.3: Distribution and Interpretation
# Distribution of Throughput per Handset Type
def distribution_and_interpretation(aggregated):
    throughput_dist = aggregated.groupby('Handset Type')['Avg_Throughput'].mean()
    tcp_dist = aggregated.groupby('Handset Type')['Avg_TCP_Retransmission'].mean()

    # Plot distributions
    plt.figure(figsize=(10, 6))
    throughput_dist.sort_values().plot(kind='bar', title='Average Throughput per Handset Type')
    plt.ylabel('Average Throughput')
    plt.show()

    plt.figure(figsize=(10, 6))
    tcp_dist.sort_values().plot(kind='bar', color='orange', title='Average TCP Retransmission per Handset Type')
    plt.ylabel('Average TCP Retransmission')
    plt.show()
    

# Task 3.4: K-Means Clustering
def k_means_clustering(aggregated,table_name_centroids, db_uri):
    # Normalize metrics
    features = ['Avg_TCP_Retransmission', 'Avg_RTT', 'Avg_Throughput']
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(aggregated[features])
    

    # Optimal k using Elbow Method
    inertia = []
    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(scaled_data)
        inertia.append(kmeans.inertia_)
        
        engine = create_engine(db_uri)

    # Convert centroids to a DataFrame for export
    centroids_df = pd.DataFrame(
        kmeans.cluster_centers_, 
        columns=['Avg_TCP_Retransmission', 'Avg_RTT', 'Avg_Throughput']
    )
    centroids_df['Cluster_Index'] = range(len(kmeans.cluster_centers_))

    # Export centroids to database
    centroids_df.to_sql(
        table_name_centroids, engine, if_exists='replace', index=False
    )
        
    # np.savetxt('experience_centroids.csv', kmeans.cluster_centers_, delimiter=',')
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 10), inertia, marker='o')
    plt.title('Elbow Method for Optimal K')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.show()
    return scaled_data;

# Apply K-Means with k=3
def apply_k_means_with_k_3(aggregated, scaled_data):
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(scaled_data)
    aggregated['Cluster'] = kmeans.labels_

    # Analyze Clusters
    cluster_summary = aggregated.groupby('Cluster').agg({
        'Avg_TCP_Retransmission': ['mean', 'min', 'max'],
        'Avg_RTT': ['mean', 'min', 'max'],
        'Avg_Throughput': ['mean', 'min', 'max']
    })

    # Visualize Clusters
    sns.pairplot(aggregated, hue='Cluster', vars=['Avg_TCP_Retransmission', 'Avg_RTT', 'Avg_Throughput'])
    plt.show()
    return cluster_summary;
