import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
load_dotenv()

db_uri = os.getenv("DATABASE_URL")

# Task 4.1: Merge engagement and experience data
def merge_data(engagement_data, experience_data):

    data = pd.merge(engagement_data, experience_data, on='MSISDN/Number')
    return data

# Task 4.1: Calculate Engagement and Experience Scores
def calculate_euclidean_scores(data, engagement_centroids, experience_centroids):
 


    # Fetch centroids and convert to NumPy arrays
    engagement_centroids = engagement_centroids.drop(columns=['Cluster_Index']).to_numpy()
    experience_centroids = experience_centroids.drop(columns=['Cluster_Index']).to_numpy()

    # Normalize data for fair distance calculation
    scaler = StandardScaler()
    normalized_engagement_data = scaler.fit_transform(data[['Session Frequency', 'Total Session Duration', 'Total Traffic']])
    normalized_experience_data = scaler.fit_transform(data[['Avg_TCP_Retransmission', 'Avg_RTT', 'Avg_Throughput']])

    # Engagement score (distance to least engaged cluster)
    least_engaged_centroid = engagement_centroids[0]  # First cluster centroid
    data['Engagement Score'] = [
        np.sqrt(np.sum((row - least_engaged_centroid) ** 2)) for row in normalized_engagement_data
    ]

    # Experience score (distance to worst experience cluster)
    worst_experience_centroid = experience_centroids[-1]  # Last cluster centroid
    data['Experience Score'] = [
        np.sqrt(np.sum((row - worst_experience_centroid) ** 2)) for row in normalized_experience_data
    ]

    return data


# Task 4.2: Calculate Satisfaction Score
def calculate_satisfaction_score(data):

    data['Satisfaction Score'] = (data['Engagement Score'] + data['Experience Score']) / 2
    top_10_satisfied = data.nlargest(10, 'Satisfaction Score')
    print("Top 10 Satisfied Customers:")
    print(top_10_satisfied[['MSISDN/Number', 'Satisfaction Score']])
    return data

# Task 4.3: Fit Regression Model
def regression_model(data):

    X = data[['Engagement Score', 'Experience Score']]
    y = data['Satisfaction Score']

    reg_model = LinearRegression()
    reg_model.fit(X, y)

    # Display regression coefficients
    print("Regression Coefficients:")
    print(f"Engagement Score Coefficient: {reg_model.coef_[0]}")
    print(f"Experience Score Coefficient: {reg_model.coef_[1]}")

    return reg_model

# Task 4.4: Perform K-Means Clustering
def kmeans_clustering(data):

    kmeans = KMeans(n_clusters=2, random_state=42)
    data['Satisfaction Cluster'] = kmeans.fit_predict(data[['Engagement Score', 'Experience Score']])

    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    plt.scatter(data['Engagement Score'], data['Experience Score'], c=data['Satisfaction Cluster'], cmap='viridis')
    plt.title('K-Means Clustering on Engagement & Experience Scores')
    plt.xlabel('Engagement Score')
    plt.ylabel('Experience Score')
    plt.show()

    return data, kmeans

# Task 4.5: Aggregate Cluster Scores
def aggregate_cluster_scores(data):

    cluster_aggregates = data.groupby('Satisfaction Cluster').agg({
        'Satisfaction Score': 'mean',
        'Experience Score': 'mean',
        'Engagement Score': 'mean'
    })

    return cluster_aggregates

# Task 4.6: Export Data to MySQL
def export_to_postgres(data, table_name):
    
    engine = create_engine(db_uri)

    # Export data to MySQL
    data[['MSISDN/Number', 'Engagement Score', 'Experience Score', 'Satisfaction Score']].to_sql(
        table_name, engine, if_exists='replace', index=False
    )

    # Verify export with a SELECT query
    query_result = pd.read_sql(f'SELECT * FROM {table_name}', con=engine)
    return query_result
