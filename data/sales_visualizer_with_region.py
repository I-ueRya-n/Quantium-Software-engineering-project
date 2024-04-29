import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Assuming you have the sales data stored in a pandas DataFrame called sales_data
# with columns 'Date', 'Region', and 'Sales'

# Replace this with your actual data
sales_data = pd.DataFrame({
    'Date': pd.date_range(start='2021-01-01', end='2021-01-31'),
    'Region': ['North', 'East', 'South', 'West'] * 8,
    'Sales': [100, 110, 120, 115, 130, 125, 135, 140, 145, 150, 155, 160, 165, 170, 
              180, 175, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 
              245, 250]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer", style={'textAlign': 'center', 'color': '#0074D9'}),
    html.Div("Filter by Region:", style={'textAlign': 'center', 'color': '#7FDBFF'}),
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'North', 'value': 'North'},
            {'label': 'East', 'value': 'East'},
            {'label': 'South', 'value': 'South'},
            {'label': 'West', 'value': 'West'},
            {'label': 'All', 'value': 'All'}
        ],
        value='All',
        labelStyle={'display': 'block', 'margin': '10px'},
        style={'textAlign': 'center', 'color': '#7FDBFF'}
    ),
    dcc.Graph(id='sales-chart'),
])

# Define callback to update the chart based on region selection
@app.callback(
    Output('sales-chart', 'figure'),
    [Input('region-filter', 'value')]
)
def update_chart(selected_region):
    if selected_region == 'All':
        filtered_sales_data = sales_data
    else:
        filtered_sales_data = sales_data[sales_data['Region'] == selected_region]
    
    traces = []
    for region, region_sales_data in filtered_sales_data.groupby('Region'):
        traces.append({
            'x': region_sales_data['Date'],
            'y': region_sales_data['Sales'],
            'type': 'scatter',
            'name': region
        })
    
    return {
        'data': traces,
        'layout': {
            'title': 'Sales Data by Region',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Sales'}
        }
    }

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
