#!/usr/bin/env python
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

def interactive_plot(data, x_col, y_col):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    scatter = ax.scatter(data[x_col], data[y_col])
    
    # Create a dropdown for selecting x and y columns
    x_dropdown = widgets.Dropdown(
        options=data.columns,
        value=x_col,
        description='X Column:',
        disabled=False
    )
    
    y_dropdown = widgets.Dropdown(
        options=data.columns,
        value=y_col,
        description='Y Column:',
        disabled=False
    )
    
    # Define a function to update the plot when dropdown values change
    def on_change(change):
        x_col = x_dropdown.value
        y_col = y_dropdown.value
        scatter.set_offsets(data[[x_col, y_col]])
        plt.draw()
    
    # Link the dropdowns to the update function
    x_dropdown.observe(on_change)
    y_dropdown.observe(on_change)
    
    display(x_dropdown)
    display(y_dropdown)
    display(fig)