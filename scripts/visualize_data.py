#!/usr/bin/env python
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

def visualize_data(data):
    # Plotting basic graphs and charts
    data.plot()
    plt.show()

if __name__ == '__main__':
    file_path = 'path_to_csv_file.csv'
    data = pd.read_csv(file_path)
    visualize_data(data)