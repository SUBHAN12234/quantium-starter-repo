import pandas as pd
import dash
from dash import Dash, html, dcc
import plotly.express as px

# Print Dash version
print(dash.__version__)

# Read multiple CSV files and concatenate into a DataFrame
df = pd.concat(
    [pd.read_csv(file, usecols=['product', 'price', 'quantity', 'date', 'region']) for file in ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']],
    ignore_index=True
)

# Remove dollar signs and convert price to float
df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)

# Calculate sales
df['sales'] = df['price'] * df['quantity']

# Filter for 'pink morsel'
pink_morsel = df[df['product'].str.contains('pink morsel', case=False, na=False)]

# Print relevant information
print(pink_morsel[['product', 'sales', 'date', 'region']])

# Create a Dash application
app = Dash(__name__)

# Create a DataFrame for Plotly
cf = pd.DataFrame({
    "date": pink_morsel['date'],
    "product": pink_morsel['product'],
    "sales": pink_morsel['sales']
})

# Create a line figure
fig = px.line(cf, x="date", y="sales", title="Sales of Pink Morsels Over Time")

# Define the layout of the Dash app
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''Dash: A web application framework for your data.'''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)

