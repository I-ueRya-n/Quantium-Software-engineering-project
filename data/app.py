import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the sales data generated from the last task
sales_data = pd.read_csv("sales_data.csv")

# Filter the data to include only the relevant period for the analysis
relevant_sales_data = sales_data[sales_data['Date'] >= '2021-01-01']

# Sort the data by date
relevant_sales_data = relevant_sales_data.sort_values(by='Date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Soul Foods Sales Visualizer'),

    dcc.Graph(
        id='sales-chart',
        figure=px.line(relevant_sales_data, x='Date', y='Sales', title='Sales Over Time')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
