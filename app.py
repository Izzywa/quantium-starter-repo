# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
sales_data = pd.read_csv('output.csv')


fig = px.line(sales_data, x='date', y='sales', title='Total Sales of Pink Morsels by Date',
              labels={
                  "sales": "Total Sales ($)",
                  "date": "Date"
              })

app.layout = html.Div(children=[
    html.H1(children='Data visualisation on the sales of the Pink Morsels'),

    
    dcc.Graph(
        id='sales-chart',
        figure=fig
    ),
    
    html.Div(children='''
        After the increase of Pink Morsel's price one 15th January 2021, the sales had increased.
    '''),

])

if __name__ == '__main__':
    app.run(debug=True)
