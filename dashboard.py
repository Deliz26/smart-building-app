import dash
from dash import html, dcc
import plotly.express as px

def create_dashboard(data, alerts):
    app = dash.Dash(__name__)
    fig_temp = px.line(data, x='timestamp', y='temperature', title='🌡️ Temperature Over Time', markers=True)
    fig_energy = px.line(data, x='timestamp', y='energy', title='⚡ Energy Consumption Over Time', markers=True)
    fig_temp.update_layout(paper_bgcolor='lavender', plot_bgcolor='white')
    fig_energy.update_layout(paper_bgcolor='mintcream', plot_bgcolor='white')

    alert_boxes = [
        html.Div(alert, style={
            'backgroundColor': '#ffcccc',
            'color': '#990000',
            'padding': '10px',
            'margin': '5px',
            'borderRadius': '8px',
            'boxShadow': '2px 2px 6px lightgray'
        }) for alert in alerts
    ]

    app.layout = html.Div(style={'backgroundColor': '#f0f8ff', 'padding': '20px'}, children=[
        html.H1("🏢 Smart Building Performance Dashboard", style={'textAlign': 'center', 'color': '#003366'}),
        html.Div([html.H4("Alerts:", style={'color': '#cc0000'})] + alert_boxes),
        dcc.Graph(figure=fig_temp),
        dcc.Graph(figure=fig_energy)
    ])
    return app