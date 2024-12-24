import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def scatter_plot(data, x_column, y_column, x_label, y_label, title):

    plt.figure(figsize=(10, 6))  # Set figure size
    sns.scatterplot(data=data, x=x_column, y=y_column)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    st.pyplot(plt)
    plt.clf()  # Clear the figure after rendering

def scatter_plots_for_apps(data, apps, y_column):

    for app in apps:
        st.subheader(f"Scatter Plot: {app} vs. {y_column}")
        scatter_plot(
            data=data,
            x_column=app,
            y_column=y_column,
            x_label=f'{app} Data (Bytes)',
            y_label=f'{y_column} (Bytes)',
            title=f'{app} vs. {y_column}'
        )
