import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("output.csv")
df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values("Date")

daily_sales = (
    df.groupby("Date")["Sales"]
    .sum()
    .reset_index()
)

fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Before and After Price Increase"
)


fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales"
)


app = dash.Dash(__name__)


app.layout = html.Div(

    children=[

        html.H1(
            "Pink Morsel Sales Visualiser"
        ),


        dcc.Graph(
            id="sales-line-chart",
            figure=fig
        )

    ]

)


if __name__ == "__main__":
    app.run(debug=True)