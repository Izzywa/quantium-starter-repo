# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])

sales_data = pd.read_csv('output.csv')

radio_button = dcc.RadioItems([
    {'label': 'East', 'value': 'east'},
    {'label': 'North', 'value': 'north'},
    {'label': 'West', 'value': 'west'},
    {'label': 'South', 'value': 'south'},
    {'label': 'All', 'value': 'all'},
], 
'all', 
id="radio_buttons",
className="d-flex justify-content-evenly"
)



app.layout = html.Div(children=[
    html.H1(children='Data visualisation on the sales of the Pink Morsels', className="m-auto", id="header"),
    
    html.Div(
      id="line_graph"
    ),
    
    html.Div([
        html.Label(children="Filter sales by region:"),
        radio_button 
    ], className="p-1",
    style={
        'border': '1px solid grey',
        'border-radius': '10px'
        }),
    
    
    html.Div([
        html.H3('Conclusion'),
        html.P("After the increase of Pink Morsel's price one 15th January 2021, the sales had increased.")
    ], className="my-3"),

], className="container py-2")

@callback (
    Output(component_id='line_graph', component_property='children'),
    Input(component_id='radio_buttons', component_property='value')
)
def update_line_graph(input_value):
    if input_value != 'all':
        filtered_data = sales_data[sales_data['region'] == input_value] 
    else:
        filtered_data = sales_data
        
    filtered_fig = px.line(filtered_data, x='date', y='sales', title=f'Total Sales of Pink Morsels by Date: {input_value.capitalize()} region',
              labels={
                  "sales": "Total Sales ($)",
                  "date": "Date"
              })
    
    return dcc.Graph(
        id='filtered-sales-chart',
        figure=filtered_fig,
        style={'width': '100%'}
    )


if __name__ == '__main__':
    app.run(debug=True)
