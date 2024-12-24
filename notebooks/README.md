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

# Task 3: Experience Analytics

    Aggregate metrics: Average TCP retransmission, RTT, throughput, and handset type (handle missing/outliers with mean/mode).
    List top 10, bottom 10, and most frequent TCP, RTT, and throughput values.
    Visualize and interpret average throughput and TCP retransmission per handset type.
    Perform k-means clustering (k=3) to segment users and describe clusters.

# Task 4: Satisfaction Analysis

    Assign engagement and experience scores using Euclidean distance.
    Calculate satisfaction as the average of engagement and experience scores; identify top 10 satisfied users.
    Build a regression model to predict satisfaction scores.
    Perform k-means clustering (k=2) on scores and aggregate satisfaction and experience per cluster.
    Export user data with scores to MySQL and provide a query screenshot.

# Task 5: Dashboard Development

    Create a Streamlit dashboard with pages for:
        User Overview, Engagement, Experience, and Satisfaction Analysis.
    Include one plot per page with interactive widgets.
    Ensure usability, interactivity, and professional design for deployment.

