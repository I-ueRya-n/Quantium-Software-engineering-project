import pandas as pd

# Load the three CSV files
sales_data_0 = pd.read_csv('data/daily_sales_data_0.csv')
sales_data_1 = pd.read_csv('data/daily_sales_data_1.csv')
sales_data_2 = pd.read_csv('data/daily_sales_data_2.csv')

# Combine the data from the three files
combined_sales_data = pd.concat([sales_data_0, sales_data_1, sales_data_2])

# Filter rows where the product is Pink Morsels
pink_morsels_data = combined_sales_data[combined_sales_data['product'] == 'Pink Morsels']

# Calculate total sales by multiplying quantity and price
pink_morsels_data['sales'] = pink_morsels_data['quantity'] * pink_morsels_data['price']

# Select and rearrange 
formatted_data = pink_morsels_data[['sales', 'date', 'region']]

# Save the formatted data into a single output file
formatted_data.to_csv('formatted_sales_data.csv', index=False)
