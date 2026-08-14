#!/usr/bin/env python
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, Javascript

def interactive_plot(data_source):
    # Fetch data from source
    df = fetch_public_data(data_source)
    
    # Create an interactive plot widget
    select_widget = widgets.Select(
        options=['Column1', 'Column2'],  # Example column names
        description='Select Column:',
        disabled=False,
    )
    display(select_widget)
    
    def on_select_change(change):
        plt.figure(figsize=(8,6))
        df[change['new']].plot()
        plt.show()
    select_widget.observe(on_select_change, names='value')

interactive_plot('your_data_source_url')