from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('../managed_data.csv')
df['date'] = pd.to_datetime(df['date'])

app.layout = html.Div([
    html.H4("Soul Food's Pink Morsel Sales"),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=df['region'].unique(),
        value=["north"],
        inline=True)
])


@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value")
)
def update_line_chart(region):
    mask = df.region.isin(region)
    fig = px.line(df[mask],
        x='date', y ="sales", title='Sales Line Chart', color='region')
    return fig


app.run_server(debug=True)