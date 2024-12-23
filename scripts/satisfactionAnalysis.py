import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Load the required data (aggregated metrics and centroids from previous tasks)
# Replace these file paths with the actual locations of your data
engagement_data = pd.read_csv('engagement_metrics.csv')
experience_data = pd.read_csv('experience_metrics.csv')
engagement_centroids = np.loadtxt('engagement_centroids.csv', delimiter=',')
experience_centroids = np.loadtxt('experience_centroids.csv', delimiter=',')

# Merge the datasets by user ID (assuming both have a common column, 'User ID')
data = pd.merge(engagement_data, experience_data, on='User ID')

# Task 4.1: Assign Engagement and Experience Scores
# Calculate Euclidean distance to the least engaged and worst experience cluster centroids
def euclidean_distance(row, centroid):
    return np.sqrt(np.sum((row - centroid) ** 2))

# Normalize data for fair distance calculation
scaler = StandardScaler()
normalized_engagement_data = scaler.fit_transform(data[['Sessions Frequency', 'Total Session Duration', 'Total Traffic']])
normalized_experience_data = scaler.fit_transform(data[['Avg_TCP_Retransmission', 'Avg_RTT', 'Avg_Throughput']])

# Engagement score (distance to least engaged cluster)
least_engaged_centroid = engagement_centroids[0]  # Adjust based on actual least engaged cluster index
data['Engagement Score'] = [euclidean_distance(row, least_engaged_centroid) for row in normalized_engagement_data]

# Experience score (distance to worst experience cluster)
worst_experience_centroid = experience_centroids[0]  # Adjust based on actual worst experience cluster index
data['Experience Score'] = [euclidean_distance(row, worst_experience_centroid) for row in normalized_experience_data]

# Task 4.2: Calculate Satisfaction Score and Identify Top 10 Satisfied Customers
data['Satisfaction Score'] = (data['Engagement Score'] + data['Experience Score']) / 2
top_10_satisfied = data.nlargest(10, 'Satisfaction Score')
print("Top 10 Satisfied Customers:")
print(top_10_satisfied[['User ID', 'Satisfaction Score']])

# Task 4.3: Regression Model to Predict Satisfaction Score
X = data[['Engagement Score', 'Experience Score']]
y = data['Satisfaction Score']

# Fit a linear regression model
reg_model = LinearRegression()
reg_model.fit(X, y)

# Display regression coefficients
print("Regression Coefficients:")
print(f"Engagement Score Coefficient: {reg_model.coef_[0]}")
print(f"Experience Score Coefficient: {reg_model.coef_[1]}")

# Task 4.4: K-Means Clustering on Engagement and Experience Scores
kmeans = KMeans(n_clusters=2, random_state=42)
data['Satisfaction Cluster'] = kmeans.fit_predict(data[['Engagement Score', 'Experience Score']])

# Visualize the clusters
plt.figure(figsize=(8, 6))
plt.scatter(data['Engagement Score'], data['Experience Score'], c=data['Satisfaction Cluster'], cmap='viridis')
plt.title('K-Means Clustering on Engagement & Experience Scores')
plt.xlabel('Engagement Score')
plt.ylabel('Experience Score')
plt.show()

# Task 4.5: Aggregate Satisfaction and Experience Scores per Cluster
cluster_aggregates = data.groupby('Satisfaction Cluster').agg({
    'Satisfaction Score': 'mean',
    'Experience Score': 'mean',
    'Engagement Score': 'mean'
})
print("Cluster Aggregates:")
print(cluster_aggregates)

# Task 4.6: Export Data to MySQL
# Database connection (adjust credentials)
engine = create_engine('mysql+pymysql://username:password@localhost/telecom_db')

# Export data to MySQL
data[['User ID', 'Engagement Score', 'Experience Score', 'Satisfaction Score']].to_sql('satisfaction_analysis', engine, if_exists='replace', index=False)

# Verify export with a SELECT query
query_result = pd.read_sql('SELECT * FROM satisfaction_analysis LIMIT 10', con=engine)
print("Database Export Verification:")
print(query_result)
