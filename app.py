import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px


# Load data
df = pd.read_csv("output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")


# Initialize app
app = dash.Dash(__name__)
server = app.server 

# Layout
app.layout = html.Div(
    style={
        "backgroundColor": "#0f172a",
        "fontFamily": "Arial",
        "padding": "20px",
        "minHeight": "100vh"
    },
    children=[

        # HEADER CARD
        html.Div(
            style={
                "textAlign": "center",
                "padding": "20px",
                "backgroundColor": "#1e293b",
                "borderRadius": "12px",
                "marginBottom": "20px"
            },
            children=[
                html.H1(
                    " Pink Morsel Sales Analytics",
                    style={"color": "white", "marginBottom": "5px"}
                ),
                html.P(
                    " Dashboard to analyze sales before & after price change",
                    style={"color": "#cbd5e1"}
                )
            ]
        ),


        # FILTER CARD
        html.Div(
            style={
                "backgroundColor": "#1e293b",
                "padding": "15px",
                "borderRadius": "12px",
                "marginBottom": "20px",
                "textAlign": "center"
            },
            children=[
                html.Label(
                    "Select Region",
                    style={"color": "white", "fontWeight": "bold"}
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "South", "value": "south"},
                        {"label": "East", "value": "east"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    labelStyle={
                             "color": "white",
                            "marginRight": "15px"
                    }
                )
            ]
        ),


        # KPI CARDS
        html.Div(
            id="kpi-cards",
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "marginBottom": "20px"
            }
        ),


        # GRAPH
        dcc.Graph(id="sales-chart")
    ]
)


# CALLBACK
@app.callback(
    [Output("sales-chart", "figure"),
     Output("kpi-cards", "children")],
    [Input("region-filter", "value")]
)
def update_dashboard(region):

    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == region]

    # Group sales
    sales = filtered.groupby("Date")["Sales"].sum().reset_index()

    total_sales = filtered["Sales"].sum()
    avg_sales = filtered["Sales"].mean()

    # LINE CHART
    fig = px.line(
        sales,
        x="Date",
        y="Sales",
        title=f"Sales Trend - {region.capitalize()}",
    )

    fig.update_layout(
        plot_bgcolor="#0f172a",
        paper_bgcolor="#0f172a",
        font_color="white",
        xaxis_title="Date",
        yaxis_title="Sales"
    )


    # KPI CARDS
    cards = [
        html.Div(
            style={
                "backgroundColor": "#1e293b",
                "padding": "15px",
                "borderRadius": "10px",
                "width": "45%",
                "textAlign": "center"
            },
            children=[
                html.H3("Total Sales", style={"color": "white"}),
                html.H2(f"{total_sales:,.0f}", style={"color": "#38bdf8"})
            ]
        ),

        html.Div(
            style={
                "backgroundColor": "#1e293b",
                "padding": "15px",
                "borderRadius": "10px",
                "width": "45%",
                "textAlign": "center"
            },
            children=[
                html.H3("Average Sales", style={"color": "white"}),
                html.H2(f"{avg_sales:,.2f}", style={"color": "#34d399"})
            ]
        )
    ]

    return fig, cards


# RUN APP
if __name__ == "__main__":
    app.run(debug=False,use_reloader=False)