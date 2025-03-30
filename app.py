<<<<<<< HEAD:app.py
=======
import os
>>>>>>> c436274 (Fixed warnings and cleaned up app.py):data/app.py
import dash
from dash import dcc, html
import dash.dependencies as dd
import pandas as pd
import plotly.express as px

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=['custom.css'])
server = app.server

# -----------------------
# Data Loading and Preprocessing
# -----------------------
<<<<<<< HEAD:app.py
df = pd.read_csv("formatted_sales_data.csv")
=======
file_path = os.path.join(os.path.dirname(__file__), "formatted_sales_data.csv")
df = pd.read_csv(file_path)
>>>>>>> c436274 (Fixed warnings and cleaned up app.py):data/app.py
# Remove the '$' symbol and convert sales to float
df["sales"] = df["sales"].replace('[\$,]', '', regex=True).astype(float)
df["date"] = pd.to_datetime(df["date"])

# Precompute daily aggregation and monthly (30-day) averages for default view
df_daily = df.groupby("date")["sales"].sum().reset_index()
df_monthly_avg = df_daily.resample("30D", on="date").mean().reset_index()
df_monthly_avg.rename(columns={"sales": "avg_sales"}, inplace=True)

# -----------------------
# App Layout with Custom Styling
# -----------------------
app.layout = html.Div([
    # Header area with pink gradient and radio buttons container
    html.Div([
        html.H1("Pink Morsel Sales Visualizer", 
                style={
                    "color": "#ffffff",
                    "textShadow": "2px 2px 4px #000000",
                    "marginBottom": "20px"
                }),
        html.Div([
            dcc.RadioItems(
                id="region-selector",
                options=[
                    {'label': "All", 'value': "all"},
                    {'label': "North", 'value': "north"},
                    {'label': "East", 'value': "east"},
                    {'label': "South", 'value': "south"},
                    {'label': "West", 'value': "west"}
                ],
                value="all",
                className="custom-radio",
                labelStyle={'display': 'inline-block', 'margin-right': '20px'}
            )
        ], style={"textAlign": "center", "padding": "10px 0"})
    ], style={
        "background": "linear-gradient(to right, #ff1493, #ff69b4)",
        "padding": "40px",
        "borderRadius": "10px",
        "marginBottom": "30px",
        "textAlign": "center"
    }),
    
    # Add a title div that will be updated by callback
    html.Div(id="graph-title", className="graph-title"),
    
    # Graph container with animate enabled for smooth transitions
    html.Div(
        dcc.Graph(id="sales-graph", animate=True, config={'displayModeBar': False}),
        style={"margin": "0 auto", "width": "90%", "height": "70vh"}
    )
], style={
    "backgroundColor": "#000000",
    "padding": "20px",
    "minHeight": "100vh"
})

# -----------------------
# Callback: Update Graph Title
# -----------------------
@app.callback(
    dd.Output("graph-title", "children"),
    [dd.Input("region-selector", "value")]
)
def update_title(selected_region):
    region_display = "All Regions" if selected_region == "all" else f"{selected_region.capitalize()} Region"
    return html.H2(f"Average Daily Sales (30-Day Periods) - {region_display}", 
                   style={"color": "#ffffff", "textAlign": "center", "marginBottom": "20px"})

# -----------------------
# Callback: Update Graph Based on Selected Region
# -----------------------
@app.callback(
    dd.Output("sales-graph", "figure"),
    [dd.Input("region-selector", "value")]
)
def update_graph(selected_region):
    # Filter data by region if not "all"
    if selected_region == "all":
        df_filtered = df.copy()
    else:
        df_filtered = df[df["region"].str.lower() == selected_region.lower()]
    
    # Aggregate daily sales for filtered data
    df_daily_filtered = df_filtered.groupby("date")["sales"].sum().reset_index()
    
    # Group into 30-day periods for monthly average
    df_monthly_avg_filtered = df_daily_filtered.resample("30D", on="date").mean().reset_index()
    df_monthly_avg_filtered.rename(columns={"sales": "avg_sales"}, inplace=True)
    
    # Calculate dynamic y-axis range for the specific filtered data
    # Add small padding to ensure line doesn't touch top/bottom
    min_y = df_monthly_avg_filtered["avg_sales"].min() * 0.9
    max_y = df_monthly_avg_filtered["avg_sales"].max() * 1.1
    
    # Create the line chart with dark template and pink line - WITHOUT a title
    fig = px.line(
        df_monthly_avg_filtered,
        x="date",
        y="avg_sales",
        labels={"avg_sales": "Average Daily Sales ($)", "date": "Date"},
        template="plotly_dark",
        color_discrete_sequence=["#ff69b4"]
    )
    
    # Clean line without markers
    fig.update_traces(
        line=dict(width=4, color="#ff69b4"),
        mode="lines",  # Remove markers, just clean line
    )
    
    # Set dynamic y-axis range based on the current region's data
    fig.update_layout(
        yaxis=dict(
            tickformat="$,.2f",
            range=[min_y, max_y],  # Dynamic y-axis range
            title="Average Daily Sales ($)",
            gridcolor="#333333"
        ),
        xaxis=dict(
            title="Date",
            gridcolor="#333333",
            # Add padding to prevent line touching y-axis
            domain=[0.02, 1]  # Start x-axis a bit after the y-axis
        ),
        transition={"duration": 800, "easing": "cubic-in-out"},
        plot_bgcolor="rgba(0,0,0,0.1)",
        paper_bgcolor="rgba(0,0,0,0)",
        hovermode="x unified",
        margin=dict(l=60, r=40, t=20, b=40),  # Reduced top margin since we have separate title
        autosize=True,
        height=580,  # Slightly reduced height to accommodate external title
        showlegend=False
    )
    
    # Add hover template for better information display
    fig.update_traces(
        hovertemplate="<b>Date:</b> %{x|%b %d, %Y}<br><b>Sales:</b> %{y:$.2f}<extra></extra>"
    )
    
    return fig

# -----------------------
# Run the App
# -----------------------
if __name__ == "__main__":
    app.run_server(debug=True)