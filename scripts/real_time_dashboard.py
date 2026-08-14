#!/usr/bin/env python
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
output_notebook()
def real_time_dashboard(data_source):
    df = pd.read_csv(StringIO(data_source))
    p = figure(title='Real-Time Data Dashboard')
    p.line(df['date'], df['value'], legend_label='Value', line_width=2)
    show(p)