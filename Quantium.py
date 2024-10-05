import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

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

# Create a Dash application
app = Dash(__name__)

# Define the layout of the Dash app
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Dashboard'),
    
    # Flex container for graph and radio items
    html.Div([
        
        # The Plotly graph
        html.Div([
            dcc.Graph(
                id='sales-graph',
            ),
        ], style={'flex': 2, 'padding': '10px'}),  # Larger flex value to make the graph wider
        
        # Radio items for region selection
        html.Div([
            html.Label('Select Region:'),
            dcc.RadioItems(
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All', 'value': 'all'}  # 'All' option to show data from all regions
                ],
                value='all',  # Default value
                id='region-selector',
            ),
        ], style={'flex': 1, 'padding': '10px', 'border': '1px solid lightgrey', 'border-radius': '10px'})
        
    ], style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'space-between'}),
    
], style={'padding': '20px'})

# Define callback to update graph based on selected region
@app.callback(
    Output('sales-graph', 'figure'),
    [Input('region-selector', 'value')]
)
def update_graph(selected_region):
    # Filter data based on selected region
    if selected_region == 'all':
        filtered_data = pink_morsel  # No filtering
    else:
        filtered_data = pink_morsel[pink_morsel['region'].str.lower() == selected_region.lower()]

    # Create updated figure
    fig = px.line(filtered_data, x='date', y='sales', title=f"Sales of Pink Morsels in {selected_region.capitalize()} Region")
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)

