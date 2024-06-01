import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load the combined dataset
df = pd.read_csv('combined_sales_data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Sales Data Visualization"),
    
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in df['region'].unique()],
        value=df['region'].unique(),
        multi=True,
        style={'width': '50%'}
    ),
    
    dcc.Graph(id='sales-time-series'),
    
    dcc.Graph(id='sales-distribution')
])

# Callback to update the time series graph based on selected regions
@app.callback(
    Output('sales-time-series', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_time_series(selected_regions):
    filtered_df = df[df['region'].isin(selected_regions)]
    fig = px.line(filtered_df, x='date', y='sales', color='region',
                  title='Sales Over Time')
    return fig

# Callback to update the sales distribution based on selected regions
@app.callback(
    Output('sales-distribution', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_sales_distribution(selected_regions):
    filtered_df = df[df['region'].isin(selected_regions)]
    fig = px.histogram(filtered_df, x='sales', color='region', 
                       title='Sales Distribution')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)