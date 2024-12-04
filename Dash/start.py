from dash import dcc, html, Dash
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate

import plotly.express as px
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

dbc_css = "http://cdn.jsdelivr.net/gh/AnMarieW/dash-bootstrap-templates/dbc.min.css"

education = pd.read_csv("./Data/states_all.csv").iloc[:, 1:]
load_figure_template("CYBORG")


app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div(style={"textAlign": "center"},
    children=[
        html.H2(
            id="Header Text", 
#            
        ),
#         html.Br(),
        html.Hr(),
        html.P("Select a State Below", id='instructions'),
        dcc.Dropdown(
                options=["Alabama", "Alaska", "Arkansas"],
                value="Alabama",
                id="State Dropdown",
                className= "dbc"
        ),
        dcc.Graph(id="Revenue Line"),
        html.P("Disclaimers: None of this data is accurate")
])

@app.callback(
    Output("Header Text", "children"),
    Output("Revenue Line", "figure"),
    Input("State Dropdown", "value")
)

def plot_bar_clar(state):
    if not state:
        raise PreventUpdate
    df=education.loc[
        (education["STATE"]==state.upper()) & (education["YEAR"].between(1992, 2017))
    ]
    fig=px.line(df,x="YEAR", y="GRADES_ALL_G")
    title = f"Enrollment over time in {state.title()}"
    return title, fig

app.run_server(debug=True, port=8111)