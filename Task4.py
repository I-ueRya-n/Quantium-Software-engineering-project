import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px



DATA_PATH = './formatted_data.csv'

DATA_PATH = "./formatted_data.csv"
COLORS = {
    "primary": "#8D02EA",
    "secondary": "#75338E",
    "font": "#F4F3F6"
}

# load in data
data = pd.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash
app = Dash(__name__)


# create the visualization
def generate_figure(chart_data):
    lineChart = px.line(chart_data, x="date", y="sales", title="Pink Morsel Sales", color_discrete_sequence=[COLORS.get("line_color", "#240581")])
    lineChart.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return lineChart


visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data)
)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

# region picker
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline = True
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "150%"
    }
)


# define the region picker callback
@app.callback(
    Output(visualization, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    # filter the dataset
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    # generate a new line chart with the filtered data
    figure = generate_figure(trimmed_data)
    return figure


# define the app layout
app.layout = html.Div(
    [
        header,
        visualization,
        region_picker_wrapper
    ],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "35px"
    }
)



if __name__ == '__main__':
    app.run(debug=True)