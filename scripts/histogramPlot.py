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