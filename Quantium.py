import pandas as pd
import os


df = pd.concat( 
    map(pd.read_csv, ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']), ignore_index=True) 
search_df = "pink morsel"
a = df[df['product'].str.contains(search_df, na=False)]
a['price'] = a['price'].str.replace(('$'), (''), regex=False).astype(float)
a['sales'] = a['price'] * a['quantity']
a = a.drop(['price', 'quantity'], axis = 1)
print(a)