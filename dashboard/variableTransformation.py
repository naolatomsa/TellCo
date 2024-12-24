import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def variable_transformation(user_aggregated):
    # Create decile segments based on total session duration
    user_aggregated['Decile'] = pd.qcut(user_aggregated['Dur. (ms)'], 5, labels=False)

    # Compute total data volume (DL + UL) per decile
    decile_data = user_aggregated.groupby('Decile').agg({
        'Total Data Volume': 'sum',
        'Dur. (ms)': 'mean'
    }).reset_index()
    return decile_data;

def plot_variable_transformation(decile_data):
    sns.barplot(data=decile_data, x='Decile', y='Total Data Volume')
    plt.title('Total Data Volume Across Deciles')
    plt.xlabel('Decile (Based on Session Duration)')
    plt.ylabel('Total Data Volume (Bytes)')
    st.pyplot(plt)