import matplotlib.pyplot as plt

def plot_histogram(data, column):
    """Plots a histogram of the specified column."""
    plt.hist(data[column].dropna(), bins=20)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column}')
    plt.show()
