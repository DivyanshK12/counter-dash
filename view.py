import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import pickle

app = dash.Dash(__name__,
                requests_pathname_prefix='/view_count/')
# df = pd.read_pickle("data.pickle")
# fig = px.scatter(df, x="Date", y="Count", color="User", size="Count")

def serve_layout():
    df = pd.read_csv("data.csv")
    fig = px.scatter(df, x="Date", y="Count", size="Count", color="User")
    return html.Div(children=[
    html.H1(children='Progress count'),

    dcc.Graph(
        id='Count',
        figure=fig)])

app.layout = serve_layout
# app.layout = html.Div(children=[
#     html.H1(children='Progress count'),

#     dcc.Graph(
#         id='Count',
#         dcc.Interval(
#             id='interval-component',
#             interval=2*60*1000, # in milliseconds , here 2 minutes
#             n_intervals=0
#         )
#     )
# ])

# @app.callback(Output('live-update-graph', 'figure'),
#               Input('interval-component', 'n_intervals'))
# def update_graph_live(n):
#     df = pd.read_pickle("data.pickle")
#     fig = px.scatter(df, x="Date", y="Count", color="User", size="Count")
#     return fig

if __name__ == '__main__':
    app.run_server(debug=True)