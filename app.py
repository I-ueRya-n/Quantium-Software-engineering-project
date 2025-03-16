import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load and preprocess data
df = pd.read_csv("formatted_sales_data.csv")

# Remove the '$' symbol and convert to float
df["sales"] = df["sales"].replace('[\$,]', '', regex=True).astype(float)
df["date"] = pd.to_datetime(df["date"])

# Step 1: Aggregate daily total sales (since one day can have many sales)
df_daily = df.groupby("date")["sales"].sum().reset_index()

# Step 2: Group the daily totals into 30-day periods and compute the average daily sales for each period
# This will give one average value per 30-day bin.
df_monthly_avg = df_daily.resample("30D", on="date").mean().reset_index()
df_monthly_avg.rename(columns={"sales": "avg_sales"}, inplace=True)

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales - 30-Day Average Daily Sales", style={'textAlign': 'center'}),
    dcc.Graph(
        id="sales-graph",
        figure=px.line(
            df_monthly_avg, 
            x="date", 
            y="avg_sales", 
            title="Average Daily Sales (30-Day Periods)",
            labels={"avg_sales": "Average Daily Sales ($)", "date": "Date"}
        ).update_layout(
            yaxis=dict(tickformat="$,.2f")
        )
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
