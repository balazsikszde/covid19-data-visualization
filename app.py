from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
data = pd.read_csv(url)
data['date'] = pd.to_datetime(data['date']).dt.date
data = data[data["continent"].notna()]
data[["new_cases", "total_cases"]] = data[[
    "new_cases", "total_cases"]].fillna(0)

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Térkép', style={'textAlign': 'center', 'fontSize': 30}),
    html.Hr(),
    dcc.Dropdown(options=['total_cases', 'total_deaths', ],
                 value='total_cases', id='controls-and-dropdown'),
    dcc.Graph(figure={}, id='controls-and-graph')
])


@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-dropdown', component_property='value')
)
def update_graph(col_chosen):
    fig = px.scatter_geo(data,
                         locations="iso_code",
                         size=col_chosen,
                         animation_frame='date',
                         height=800,
                         size_max=50,
                         color="continent"
                         )
    fig.update_geos(showcountries=True)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
