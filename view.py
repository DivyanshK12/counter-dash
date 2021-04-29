import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__,
                requests_pathname_prefix='/view_count/')
df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Date", y="Count", color="User", size="Count")

app.layout = html.Div(children=[
    html.H1(children='Progress count'),

    dcc.Graph(
        id='Count',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)