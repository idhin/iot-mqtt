import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import datetime
import numpy as np

app = dash.Dash(__name__)
app.layout = html.Div(

    html.Div([

        html.Div([
            dcc.Graph(id='acc-update-graph'),
            dcc.Interval(
                id='interval-component',
                interval=1 * 1000,  # in milliseconds
                n_intervals=0,
            )
        ],
            style={'display': 'inline-block', 'padding': '0 20 0 0'}),

        # html.Div([
        #     dcc.Graph(id='accMA-update-graph')
        # ],
        #     style={'display': 'inline-block', 'padding': '0 20 0 0'}),
        #
        # html.Div([
        #     dcc.Graph(id='gyr-update-graph')
        # ],
        #     style={'display': 'inline-block', 'padding': '0 20 0 0'}),

        html.Div([
            dcc.Graph(id='gyrMA-update-graph')
        ],
            style={'display': 'inline-block', 'padding': '0 20 0 0'}),

        html.Div([
            dcc.Graph(id='comp-update-graph')
        ],
            style={'display': 'inline-block', 'padding': '0 20 0 0'})

    ]),

)


@app.callback(Output('acc-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
# def update_graph_acc(n):
#     df = pd.read_csv('dataRiset.csv', encoding='utf-8')
#     fig = {
#         'data': [
#             {'x': df['time'], 'y': df['accx'], 'type': 'line', 'name': 'Accelerometer X'},
#             {'x': df['time'], 'y': df['accy'], 'type': 'line', 'name': 'Accelerometer Y'},
#             {'x': df['time'], 'y': df['accz'], 'type': 'line', 'name': 'Accelerometer Z'}
#         ],
#         'layout': {
#             'width': 1400,
#             'height': 400,
#             'title': 'Linear Accelerometer',
#             'yaxis': dict(title='Accelerometer (g)'),
#             'xaxis': dict(autorange=True,
#                           showgrid=False,
#                           zeroline=False,
#                           showline=False,
#                           ticks='',
#                           title='Time (s)',
#                           showticklabels=False),
#             'showlegend': True
#         }
#     }
# 
#     return fig
# 
# 
# @app.callback(Output('gyr-update-graph', 'figure'),
#               [Input('interval-component', 'n_intervals')])
# def update_graph_gyr(n):
#     df = pd.read_csv('dataRiset.csv', encoding='utf-8')
#     figure = {
#         'data': [
#             {'x': df['time'], 'y': df['gyrx'], 'type': 'line', 'name': 'Gyroscope X'},
#             {'x': df['time'], 'y': df['gyry'], 'type': 'line', 'name': 'Gyroscope Y'},
#             {'x': df['time'], 'y': df['gyrz'], 'type': 'line', 'name': 'Gyroscope Z'}
#         ],
#         'layout': {
#             'width': 1400,
#             'height': 400,
#             'title': 'Linear Gyroscope',
#             'yaxis': dict(title='Gyroscope (deg/s)'),
#             'xaxis': dict(autorange=True,
#                           showgrid=False,
#                           zeroline=False,
#                           showline=False,
#                           ticks='',
#                           title='Time (s)',
#                           showticklabels=False),
#             'showlegend': True
#         }
#     }
# 
#     return figure
# 
# 
# @app.callback(Output('accMA-update-graph', 'figure'),
#               [Input('interval-component', 'n_intervals')])
def update_graph_accMA(n):
    df = pd.read_csv('dataRiset.csv', encoding='utf-8')
    df['accxMA'] = df['accx'].rolling(window=50).mean()
    df['accyMA'] = df['accy'].rolling(window=50).mean()
    df['acczMA'] = df['accz'].rolling(window=50).mean()

    figMA = {
        'data': [
            {'x': df['time'], 'y': df['accxMA'], 'type': 'line', 'name': 'MA Accelerometer X'},
            {'x': df['time'], 'y': df['accyMA'], 'type': 'line', 'name': 'MA Accelerometer Y'},
            {'x': df['time'], 'y': df['acczMA'], 'type': 'line', 'name': 'MA Accelerometer Z'}
        ],
        'layout': {
            'width': 1400,
            'height': 400,
            'title': 'Moving Average (50 Data/Block) Filter on Accelerometer Data',
            'yaxis': dict(title='Accelerometer (g)'),
            'xaxis': dict(autorange=True,
                          showgrid=False,
                          zeroline=False,
                          showline=False,
                          ticks='',
                          title='Time (s)',
                          showticklabels=False),
            'showlegend': True
        }
    }

    return figMA


@app.callback(Output('gyrMA-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_gyrMA(n):
    df = pd.read_csv('dataRiset.csv', encoding='utf-8')
    df['gyrxMA'] = df['gyrx'].rolling(window=50).mean()
    df['gyryMA'] = df['gyry'].rolling(window=50).mean()
    df['gyrzMA'] = df['gyrz'].rolling(window=50).mean()
    figureMA = {
        'data': [
            {'x': df['time'], 'y': df['gyrxMA'], 'type': 'line', 'name': 'MA Gyroscope X'},
            {'x': df['time'], 'y': df['gyryMA'], 'type': 'line', 'name': 'MA Gyroscope Y'},
            {'x': df['time'], 'y': df['gyrzMA'], 'type': 'line', 'name': 'MA Gyroscope Z'}
        ],
        'layout': {
            'width': 1400,
            'height': 400,
            'title': 'Moving Average (50 Data/Block) Filter on Gyroscope Data',
            'yaxis': dict(title='Gyroscope (deg/s)'),
            'xaxis': dict(autorange=True,
                          showgrid=False,
                          zeroline=False,
                          showline=False,
                          ticks='',
                          title='Time (s)',
                          showticklabels=False),
            'showlegend': True
        }
    }

    return figureMA


@app.callback(Output('comp-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_comp(n):
    df = pd.read_csv('dataRiset.csv', encoding='utf-8')
    df['accxMA'] = df['accx'].rolling(window=50).mean()
    df['accyMA'] = df['accy'].rolling(window=50).mean()
    df['acczMA'] = df['accz'].rolling(window=50).mean()
    df['gyrxMA'] = df['gyrx'].rolling(window=50).mean()
    df['gyryMA'] = df['gyry'].rolling(window=50).mean()
    df['gyrzMA'] = df['gyrz'].rolling(window=50).mean()
    accroll = np.arctan2(df['accyMA'], df['acczMA'])
    accpitch = np.arctan2(-(df['accxMA']), np.sqrt(df['accyMA'] * df['accyMA'] + df['acczMA'] * df['acczMA']))
    accyaw = np.arctan2(df['acczMA'], np.sqrt(df['accxMA'] * df['accxMA'] + df['acczMA'] * df['acczMA']))
    df['accroll'] = np.arctan2(df['accyMA'], df['acczMA']) - 2.5
    df['accpitch'] = np.arctan2(-(df['accxMA']), np.sqrt(df['accyMA'] * df['accyMA'] + df['acczMA'] * df['acczMA']))
    df['accyaw'] = np.arctan2(df['acczMA'], np.sqrt(df['accxMA'] * df['accxMA'] + df['acczMA'] * df['acczMA']))
    dt = 0.02
    gyrpitch = df['gyryMA'] * dt
    gyrroll = df['gyrxMA'] * dt
    gyryaw = df['gyrzMA'] * dt
    df['gyrpitch'] = df['gyryMA'] * dt
    df['gyrroll'] = (df['gyrxMA'] * dt)
    df['gyryaw'] = (df['gyrzMA'] * dt)
    df['pitch'] = gyrpitch * 0.98 + accpitch * 0.02
    df['roll'] = gyrroll * 0.98 + accroll * 0.02
    df['yaw'] = gyryaw * 0.98 + accyaw * 0.02
    df['dg'] = df['pitch'] * 90
    figureC = {
        'data': [
            {'x': df['time'], 'y': df['accpitch'], 'type': 'line', 'name': 'Accel'},
            {'x': df['time'], 'y': df['gyrpitch'], 'type': 'line', 'name': 'Gyro'},
            {'x': df['time'], 'y': df['dg'], 'type': 'line', 'name': 'Complementary Filter'}
        ],
        'layout': {
            'width': 1400,
            'height': 400,
            'title': 'Complementary Filter',
            'yaxis': dict(title='degree'),
            'xaxis': dict(autorange=True,
                          showgrid=False,
                          zeroline=False,
                          showline=False,
                          ticks='',
                          title='Time (s)',
                          showticklabels=False),
            'showlegend': True
        }
    }

    return figureC


# Dash CSS
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
# Loading screen CSS
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})

if __name__ == '__main__':
    app.run_server()
