#!/usr/bin/env python
import dash
import pandas as pd
from dash import dcc, html
from dash.dependencies import Input, Output
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0
    )
])
def generate_graph(n):
    df = pd.read_csv('data.csv')
    fig = px.line(df, x='date', y='value')
    return fig
app.callback(Output('live-update-graph', 'figure'), [Input('interval-component', 'n_intervals')])(generate_graph)
if __name__ == '__main__':
    app.run_server(debug=True)