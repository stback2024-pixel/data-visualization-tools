#!/usr/bin/env python
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, Javascript

# Function to load data from a CSV file or URL
@widgets.interact
def load_data(file_or_url=widgets.Text(value='https://raw.githubusercontent.com/stback2024-pixel/data-visualization-tools/main/demos/sample.csv', description='File/URL')):
    if 'http' in file_or_url:
        data = pd.read_csv(file_or_url)
    else:
        with open(file_or_url, 'r') as f:
            data = pd.read_csv(f)
    return data

# Function to visualize data interactively
@widgets.interact
def visualize_data(data=load_data()):
    plt.figure()
    data.plot(kind='line', marker='o')
    plt.show()