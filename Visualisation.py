import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px



DATA_PATH = './formatted_data.csv'

data = pd.read_csv(DATA_PATH)
data = data.sort_values(by = 'date')

app = Dash()

lineChart = px.line(data, x = 'date', y = 'sales', title = 'Pink morsel Sales')
visualisation = dcc.Graph(
    id = 'Visualistion',
    figure = lineChart
)

header = html.H1(
    'PINK MORSEL SALES',
    id = 'header'
)


app.layout = html.Div(
    [
        header,
        visualisation
    ]
)


if __name__ == '__main__':
    app.run(debug=True)