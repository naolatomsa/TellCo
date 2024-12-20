# Task 1: User Overview Analysis

    Identified:
        Top 10 handsets and top 3 handset manufacturers.
        Top 5 handsets for each of the top 3 manufacturers.
    Aggregated user metrics:
        Number of xDR sessions, session duration, total download/upload data per user, and total traffic per application.
    Conducted Exploratory Data Analysis (EDA):
        Univariate Analysis: Examined dispersion metrics (mean, median, etc.) and visualized distributions.
        Bivariate Analysis: Explored relationships between application usage and total data volume.
        PCA: Reduced data dimensions, retaining ~71% variance for simplified clustering.

# Task 2: User Engagement Analysis

    Aggregated metrics per user:
        Session frequency, session duration, and total traffic.
    Performed k-means clustering (k=3):
        Classified users into low, moderate, and high engagement clusters.
        Visualized clusters and calculated cluster-wise statistics (min, max, mean, total).
    Application-level analysis:
        Identified the top 10 most engaged users per application.
        Visualized the top 3 most used applications.
    Optimized clustering:
        Used the Elbow Method to confirm 3 optimal clusters.

