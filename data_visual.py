import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Assuming you have the sales data stored in a pandas DataFrame called sales_data
# with columns 'Date' and 'Sales'

# Replace this with your actual data
sales_data = pd.DataFrame({
    'Date': pd.date_range(start='2021-01-01', end='2021-01-31'),
    'Sales': [100, 110, 120, 115, 130, 125, 135, 140, 145, 150, 155, 160, 165, 170, 
              180, 175, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 
              245, 250]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer"),
    dcc.Graph(id='sales-chart'),
])

# Define callback to update the chart
@app.callback(
    Output('sales-chart', 'figure'),
    [Input('sales-chart', 'value')]
)
def update_chart(selected_value):
    # Filter data before and after the price increase
    sales_before = sales_data[sales_data['Date'] < '2021-01-15']
    sales_after = sales_data[sales_data['Date'] >= '2021-01-15']
    
    # Create traces for before and after
    trace_before = {
        'x': sales_before['Date'],
        'y': sales_before['Sales'],
        'type': 'scatter',
        'name': 'Before Price Increase'
    }
    trace_after = {
        'x': sales_after['Date'],
        'y': sales_after['Sales'],
        'type': 'scatter',
        'name': 'After Price Increase'
    }
    
    # Return figure
    return {
        'data': [trace_before, trace_after],
        'layout': {
            'title': 'Sales Before and After Price Increase',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Sales'}
        }
    }

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
