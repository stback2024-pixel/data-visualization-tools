#!/usr/bin/env python
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import curdoc
def load_data(file_path):
    return pd.read_csv(file_path)
def create_plot(data): 
    p = figure(title='Interactive Data Visualization', x_axis_label='X Axis', y_axis_label='Y Axis')
    p.line(data['x'], data['y'], legend_label='Temp.', line_width=2)
    return p
file_path = 'demos/interactive_dataset_demo.csv'
data = load_data(file_path)
p = create_plot(data)
curdoc().add_root(p)