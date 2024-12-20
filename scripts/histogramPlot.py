import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_histogram(data, column_name):
    # Create a histogram and density plot for 'Avg RTT UL (ms)'
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column_name], kde=True, color='green', bins=10)
    plt.title('Distribution of Avg RTT UL (ms)')
    plt.xlabel('Avg RTT UL (ms)')
    plt.ylabel('Frequency')
    plt.show()
    
def total_data_volume_distribution(user_aggregated, title, xlabel, ylabel):
    sns.histplot(user_aggregated['Total Data Volume'], kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    
def distribution_of_app_usage(usage_stats, title, xlabel, ylabel, app):
    if app=='app':
        usage_stats.plot(kind='bar')
    else:
        usage_stats['Total Data Volume']['mean'].plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    


def plot(user_aggregated):

    # Boxplot for 'Dur. (ms)'
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=user_aggregated['Dur. (ms)'], color='skyblue')
    plt.title('Boxplot of Session Durations (Dur. (ms))', fontsize=14)
    plt.xlabel('Session Duration (ms)', fontsize=12)
    plt.show()

    # Boxplot for 'Total Data Volume'
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=user_aggregated['Total Data Volume'], color='orange')
    plt.title('Boxplot of Total Data Volume', fontsize=14)
    plt.xlabel('Total Data Volume (Bytes)', fontsize=12)
    plt.show()

    # Histogram for 'Dur. (ms)'
    plt.figure(figsize=(8, 6))
    sns.histplot(user_aggregated['Dur. (ms)'], bins=20, kde=True, color='blue')
    plt.title('Histogram of Session Durations (Dur. (ms))', fontsize=14)
    plt.xlabel('Session Duration (ms)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.show()

    # Histogram for 'Total Data Volume'
    plt.figure(figsize=(8, 6))
    sns.histplot(user_aggregated['Total Data Volume'], bins=20, kde=True, color='green')
    plt.title('Histogram of Total Data Volume', fontsize=14)
    plt.xlabel('Total Data Volume (Bytes)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.show()


def top_3_most_used_app(user_aggregated, app_columns):
    # Identify the total traffic per application
    total_traffic_per_app = user_aggregated[app_columns].sum().sort_values(ascending=False)

    # Plot the top 3 most used applications
    top_3_apps = total_traffic_per_app.head(3)
    top_3_apps.plot(kind='bar', color=['blue', 'green', 'orange'], figsize=(10, 6))
    plt.title('Top 3 Most Used Applications')
    plt.ylabel('Total Traffic (Bytes)')
    plt.xlabel('Applications')
    plt.show()