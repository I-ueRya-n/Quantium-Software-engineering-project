import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Read the data
df = pd.read_csv('formatted_data.csv', sep=';', parse_dates=['date'])
# Ensure your CSV has a 'region' column to filter by region

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Sales Visualizer for Soul Foods'),

    html.Label('Select Region:'),
    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',  # Default value
        style={"padding": "20px"}
    ),

    dcc.Graph(id='sales-line-chart')
])

# Callback to update line chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_figure(selected_region):
    filtered_df = df if selected_region == 'all' else df[df['region'] == selected_region]
    
    # Create a line chart
    fig = px.line(filtered_df, x='date', y='sales', title='Pink Morsels Sales Over Time',
                  labels={'sales': 'Sales', 'date': 'Date'})
    
    # Highlight the date of price increase
    fig.add_vline(x='2021-01-15', line_width=2, line_dash="dash", line_color="red")
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)