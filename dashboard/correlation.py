import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def correlation_matrix(user_aggregated, app_columns):
    correlation_matrix = user_aggregated[app_columns].corr()

    # Heatmap visualization
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Applications')
    st.pyplot(plt)