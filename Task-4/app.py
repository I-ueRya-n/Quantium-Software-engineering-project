import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load the combined dataset
df = pd.read_csv('combined_sales_data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

# Layout of the Dash app
app.layout = html.Div(style={'fontFamily': 'Arial', 'padding': '10px'}, children=[
    html.H1("Sales Data Visualization", style={'textAlign': 'center', 'color': '#333'}),
    
    html.Div([
        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'padding': '10px', 'fontSize': '18px'}
        )
    ], style={'textAlign': 'center', 'padding': '20px'}),
    
    html.Div([
        dcc.Graph(id='sales-time-series')
    ], style={'padding': '20px'}),
    
    html.Div([
        dcc.Graph(id='sales-distribution')
    ], style={'padding': '20px'})
])

# Callback to update the time series graph based on selected region
@app.callback(
    Output('sales-time-series', 'figure'),
    [Input('region-radio', 'value')]
)
def update_time_series(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    fig = px.line(filtered_df, x='date', y='sales', color='region',
                  title='Sales Over Time')
    return fig

# Callback to update the sales distribution based on selected region
@app.callback(
    Output('sales-distribution', 'figure'),
    [Input('region-radio', 'value')]
)
def update_sales_distribution(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    fig = px.histogram(filtered_df, x='sales', color='region', 
                       title='Sales Distribution')
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)