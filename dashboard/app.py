from dotenv import load_dotenv
from sqlalchemy import create_engine
import streamlit as st
import pandas as pd
import os
load_dotenv()

db_uri = os.getenv("DATABASE_URL")
engine = create_engine(db_uri)

query = "SELECT * FROM xdr_data;"

query_engagement_data = "SELECT * FROM engagement_metrics;"
query_experience_data = "SELECT * FROM experience_metrics;"
query_engagement_centroids = "SELECT * FROM engagement_centroids;"
query_experience_centroids = "SELECT * FROM experience_centroids;"

data = pd.read_sql(query, con=engine)

engagement_data =  pd.read_sql(query_engagement_data, con=engine)
experience_data =  pd.read_sql(query_experience_data, con=engine)
engagement_centroids =  pd.read_sql(query_engagement_centroids, con=engine)
experience_centroids =  pd.read_sql(query_experience_centroids, con=engine)




def main():
    # Configure page
    st.set_page_config(page_title="Streamlit Dashboard", layout="wide")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    nav_option = st.sidebar.radio("Go to", ["Home", "User Overview Analysis", "User Engagement Analysis", "Experience Analytics", "Satisfaction Analysis"])

    # Display content based on navigation
    if nav_option == "Home":
        show_home()
    elif nav_option == "User Overview Analysis":
        show_User_Overview_Analysis()
    elif nav_option == "User Engagement Analysis":
        show_User_Engagement_Analysis()
    elif nav_option == "Experience Analytics":
        show_Experience_Analytics()
    elif nav_option == "Satisfaction Analysis":
        show_Satisfaction_Analysis()

#task 1
def aggregate_per_user():
    st.subheader("Aggregate Per User Analysis")
    st.write(data.head(10))
    st.write("Displaying aggregate analysis per user...")
    # Add your logic or visualizations for aggregate analysis here

def exploratory_data_analysis():
    st.subheader("Exploratory Data Analysis")
    st.write("Displaying exploratory data analysis...")
    # Add your logic or visualizations for EDA here


#task 3
def aggregate_per_customer():
    st.subheader("Aggregate Per Customer Analysis")
    st.write("Displaying aggregate analysis per customer...")
    # Add your logic or visualizations for aggregate analysis here

def top_bottom_most_frequent():
    st.subheader("Top, Bottom, and Most Frequent Analysis")
    st.write("Displaying top 10, bottom 10, and most frequent items...")
    # Add your logic or visualizations here

def distribution_interpretation():
    st.subheader("Distribution and Interpretation")
    st.write("Displaying data distribution and its interpretation...")
    # Add your logic or visualizations here

def k_means_clustering():
    st.subheader("K-Means Clustering")
    st.write("Displaying K-Means Clustering results...")
    # Add your logic or visualizations here



#task 4
def engagement_experience_score():
    st.subheader("Engagement and Experience Score")
    st.write("Displaying engagement and experience score analysis...")
    # Add specific logic for engagement and experience analysis here

def satisfaction_score():
    st.subheader("Satisfaction Score")
    st.write("Displaying satisfaction score analysis...")
    st.write(engagement_data.head(10))
    st.write(experience_data.head(10))
    st.write(engagement_centroids.head(10))
    st.write(experience_centroids.head(10))

    
    # Add specific logic for satisfaction score analysis here

def fit_regression_model():
    st.subheader("Fit Regression Model")
    st.write("Fitting and displaying regression model results...")
    # Add specific logic for regression model analysis here

def perform_k_means_clustering():
    st.subheader("Perform K-Means Clustering")
    st.write("Performing K-Means Clustering and displaying results...")
    # Add specific logic for K-Means clustering analysis here

def aggregate_cluster_score():
    st.subheader("Aggregate Cluster Score")
    st.write("Displaying aggregate cluster score analysis...")
    # Add specific logic for aggregate cluster score analysis here

def exported_data():
    st.subheader("Exported Data")
    st.write("Displaying exported data...")
    # Add specific logic for exported data here
    
#home
def show_home():
    st.title("Welcome to the Telecom User Analysis")
    st.info("Use the navigation menu to explore other sections.")

def show_User_Overview_Analysis():
    st.title("Analytics Page")
    st.write("Here, you can analyze your data.")
    user_overview_analysis = st.selectbox("Select", ["Aggregate per user", "Exploratory Data Analysis"])
    # st.write(f"Language: {user_overview_analysis}")
    
    if user_overview_analysis == "Aggregate per user":
        aggregate_per_user()
    elif user_overview_analysis == "Exploratory Data Analysis":
        exploratory_data_analysis()
    
    # st.metric(label="Total Sales", value="$100,000", delta="+5%")
    # st.metric(label="Active Users", value="1,200", delta="+50")

def show_User_Engagement_Analysis():
    st.title("Visualization Page")
    st.write("Visualize your data with interactive charts.")
    # Example plot using matplotlib
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="Sine Wave")
    ax.legend()

    st.pyplot(fig)
def show_Experience_Analytics():
    st.title("Settings Page")
    st.write("Configure your preferences here.")
    # dark_mode = st.checkbox("Enable Dark Mode")
    # language = st.selectbox("Select Language", ["English", "Spanish", "French"])

    # st.write("Your settings:")
    # st.write(f"Dark Mode: {'Enabled' if dark_mode else 'Disabled'}")
    # st.write(f"Language: {language}")
    
    Experience_Analytics = st.selectbox("Select", ["Aggregate per customer", "10 of the top, bottom, and most frequent", "Distribution and Interpretation", "K-Means Clustering"])

    # Display functions based on selection
    if Experience_Analytics == "Aggregate per customer":
        aggregate_per_customer()
    elif Experience_Analytics == "10 of the top, bottom, and most frequent":
        top_bottom_most_frequent()
    elif Experience_Analytics == "Distribution and Interpretation":
        distribution_interpretation()
    elif Experience_Analytics == "K-Means Clustering":
        k_means_clustering()
    
def show_Satisfaction_Analysis():
    st.title("Settings Page")
    st.write("Configure your preferences here.")
    
    Satisfaction_Analysis = st.selectbox("Select", ["Engagement and Exprience Score", "Satisfaction Score", "Fit-Regression Model", "Perform K-Means Clustering", "Aggregate Cluster Score", "Exported Data"])
    
        # Display functions based on selection
    if Satisfaction_Analysis == "Engagement and Exprience Score":
        engagement_experience_score()
    elif Satisfaction_Analysis == "Satisfaction Score":
        satisfaction_score()
    elif Satisfaction_Analysis == "Fit-Regression Model":
        fit_regression_model()
    elif Satisfaction_Analysis == "Perform K-Means Clustering":
        perform_k_means_clustering()
    elif Satisfaction_Analysis == "Aggregate Cluster Score":
        aggregate_cluster_score()
    elif Satisfaction_Analysis == "Exported Data":
        exported_data()

if __name__ == "__main__":
    main()
