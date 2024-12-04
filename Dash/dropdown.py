import pandas as pd
from dash import html, dcc, Dash
from dash.dependencies import Output, Input

education = pd.read_csv("./Data/states_all.csv", usecols=["STATE", "YEAR", "TOTAL_EXPENDITURE"])
selecao = (education["STATE"] == "WASHINGTON") & (education["YEAR"] > 1992)
df = education[selecao]

app = Dash(__name__)

app.layout = html.Div([
    html.H3("Select a State: "),
    dcc.Dropdown(options=["California", "Oregon", "Washington"], value="California", id="state-dropdown"),
    html.H3(children="Selected State: ", id="text-state")
])

@app.callback(
    Output(component_id="text-state" ,component_property="children"),
    Input(component_id="state-dropdown" ,component_property="value" )
)
def text_update(state):
    return f"Selected State: {state}"

if __name__ == "__main__":
    app.run_server(debug=True)