from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def DR_PCA(user_aggregated,app_columns):
    # Standardize the application data
    scaler = StandardScaler()
    app_data_scaled = scaler.fit_transform(user_aggregated[app_columns])

    # Perform PCA
    pca = PCA(n_components=2)
    
    principal_components = pca.fit_transform(app_data_scaled)

    # Explained variance
    explained_variance = pca.explained_variance_ratio_

    # Output PCA results
    return explained_variance;
