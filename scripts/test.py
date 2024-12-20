import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load dataset (replace 'data.csv' with your file)
data = pd.read_csv('data.csv')

# Task 1: Top Handsets and Manufacturers
# Top 10 Handsets
top_10_handsets = data['Handset Type'].value_counts().head(10)

# Top 3 Manufacturers
top_3_manufacturers = data['Handset Manufacturer'].value_counts().head(3)

# Top 5 Handsets per Top 3 Manufacturers
top_5_per_manufacturer = {}
for manufacturer in top_3_manufacturers.index:
    top_5_per_manufacturer[manufacturer] = data[data['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)

# Task 1.1: User Behavior on Applications
# Aggregate per user
data['Total Data Volume'] = data['DL Volume (Bytes)'] + data['UL Volume (Bytes)']
user_aggregated = data.groupby('User ID').agg({
    'Session ID': 'count',  # Number of xDR sessions
    'Session Duration': 'sum',  # Total session duration
    'DL Volume (Bytes)': 'sum',  # Total download volume
    'UL Volume (Bytes)': 'sum',  # Total upload volume
    'Total Data Volume': 'sum',  # Total data volume
    'Social Media': 'sum',
    'Google': 'sum',
    'Email': 'sum',
    'YouTube': 'sum',
    'Netflix': 'sum',
    'Gaming': 'sum',
    'Other': 'sum'
}).reset_index()

# Task 1.2: Exploratory Data Analysis
# Describe variables and data types
description = data.describe()
data_types = data.dtypes

# Handle missing values
missing_values = data.isnull().sum() / len(data) * 100
data.fillna(data.mean(), inplace=True)

# Identify and handle outliers using IQR
numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
for col in numerical_columns:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data[col] = np.where(data[col] < lower_bound, data[col].mean(), data[col])
    data[col] = np.where(data[col] > upper_bound, data[col].mean(), data[col])

# Decile segmentation
user_aggregated['Decile'] = pd.qcut(user_aggregated['Session Duration'], 10, labels=False)
decile_data = user_aggregated.groupby('Decile').agg({'Total Data Volume': 'sum'}).reset_index()

# Basic metrics
metrics = user_aggregated[['Session Duration', 'DL Volume (Bytes)', 'UL Volume (Bytes)', 'Total Data Volume']].agg(['mean', 'median', 'std', 'var'])

# Non-Graphical Univariate Analysis
dispersion = user_aggregated[['Session Duration', 'DL Volume (Bytes)', 'UL Volume (Bytes)', 'Total Data Volume']].describe()

# Graphical Univariate Analysis
for col in ['Session Duration', 'DL Volume (Bytes)', 'UL Volume (Bytes)', 'Total Data Volume']:
    plt.figure()
    sns.histplot(user_aggregated[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

# Bivariate Analysis
bivariate_data = user_aggregated[['Social Media', 'Google', 'Email', 'YouTube', 'Netflix', 'Gaming', 'Other', 'Total Data Volume']]
sns.pairplot(bivariate_data)
plt.show()

# Correlation Analysis
correlation_matrix = bivariate_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Dimensionality Reduction using PCA
scaler = StandardScaler()
bivariate_scaled = scaler.fit_transform(bivariate_data.drop(columns=['Total Data Volume']))
pca = PCA(n_components=2)
principal_components = pca.fit_transform(bivariate_scaled)
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_explained_variance = pca.explained_variance_ratio_

# PCA Interpretation
pca_summary = {
    'Explained Variance Ratio': pca_explained_variance,
    'Top Contributing Features (PC1)': np.argsort(-pca.components_[0])[:3],
    'Top Contributing Features (PC2)': np.argsort(-pca.components_[1])[:3]
}

# Outputs
print("Top 10 Handsets:")
print(top_10_handsets)

print("Top 3 Manufacturers:")
print(top_3_manufacturers)

print("Top 5 Handsets per Top 3 Manufacturers:")
for manufacturer, handsets in top_5_per_manufacturer.items():
    print(f"{manufacturer}:\n{handsets}\n")

print("PCA Summary:")
print(pca_summary)
