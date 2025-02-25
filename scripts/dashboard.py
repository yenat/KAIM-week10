import dash
from dash import dcc, html
import dash.dependencies as dd
import pandas as pd
import requests
import plotly.graph_objs as go

# Fetch data from the Flask API
response = requests.get('http://127.0.0.1:5001/api/data')
data = response.json()
df = pd.DataFrame(data)

# Convert the Date column to datetime format and handle non-date values
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date'], inplace=True)

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Brent Oil Prices Dashboard"),
    dcc.DatePickerRange(
        id='date-range',
        start_date=df['Date'].min().date(),
        end_date=df['Date'].max().date()
    ),
    dcc.Graph(id='price-graph'),
    dcc.Graph(id='gdp-graph'),
    dcc.Graph(id='unemployment-graph'),
])

# Callback to update the graphs based on selected date range
@app.callback(
    [dd.Output('price-graph', 'figure'),
     dd.Output('gdp-graph', 'figure'),
     dd.Output('unemployment-graph', 'figure')],
    [dd.Input('date-range', 'start_date'),
     dd.Input('date-range', 'end_date')]
)
def update_graphs(start_date, end_date):
    # Ensure the dates are in proper format
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    price_fig = go.Figure(data=[go.Scatter(x=filtered_df['Date'], y=filtered_df['Price'], mode='lines', name='Brent Oil Price')])
    price_fig.update_layout(title='Brent Oil Prices', xaxis_title='Date', yaxis_title='Price')

    gdp_fig = go.Figure(data=[go.Scatter(x=filtered_df['Date'], y=filtered_df['GDP'], mode='lines', name='GDP')])
    gdp_fig.update_layout(title='GDP Over Time', xaxis_title='Date', yaxis_title='GDP (current US$)')

    unemployment_fig = go.Figure(data=[go.Scatter(x=filtered_df['Date'], y=filtered_df['Unemployment Rate'], mode='lines', name='Unemployment Rate')])
    unemployment_fig.update_layout(title='Unemployment Rate Over Time', xaxis_title='Date', yaxis_title='Unemployment Rate (%)')

    return price_fig, gdp_fig, unemployment_fig

if __name__ == '__main__':
    app.run_server(debug=True, port=5002)
