import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import pickle

app = dash.Dash(__name__,
                requests_pathname_prefix='/view_count/')

def serve_layout():
    df = pd.read_csv("data.csv")
    fig = px.scatter(df, x="Date", y="Count", size="Count", color="User")
    return html.Div(children=[
    html.H1(children='Progress count'),

    dcc.Graph(
        id='Count',
        figure=fig)])

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True)