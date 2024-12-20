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