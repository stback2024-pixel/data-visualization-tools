#!/usr/bin/env python
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_notebook
output_notebook()

def load_and_visualize():
    # Load data from CSV file or public dataset
    df = pd.read_csv('data.csv')
    
    # Convert to Bokeh's ColumnDataSource for interactivity
    source = ColumnDataSource(df)
    
    # Create a basic plot with hover tools for interactivity
    p = figure(title='Interactive Data Explorer', x_axis_label='X-axis', y_axis_label='Y-axis')
    p.circle('x_column', 'y_column', source=source, size=5, color='blue', alpha=0.6)
    
    hover = HoverTool(tooltips=[('index', '$index'), ('(x,y)', '($x, $y)'), ('value', '@value')])
    p.add_tools(hover)

    show(p)

if __name__ == '__main__':
    load_and_visualize()