import pandas as pd
import os

# Function to read CSV file with error handling
def read_csv_with_error_handling(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# File paths
file_paths = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

# Load the three CSV files
sales_data = [read_csv_with_error_handling(file_path) for file_path in file_paths]

# Check if any file failed to load
if any(data is None for data in sales_data):
    print("Error: One or more files failed to load. Exiting.")
    exit()

# Combine the data from the three files
combined_sales_data = pd.concat(sales_data)

# Filter rows where the product is Pink Morsels
pink_morsels_data = combined_sales_data[combined_sales_data['product'] == 'Pink Morsels']

# Calculate total sales by multiplying quantity and price
pink_morsels_data['sales'] = pink_morsels_data['quantity'] * pink_morsels_data['price']

# Select and rearrange 
formatted_data = pink_morsels_data[['sales', 'date', 'region']]

# Save the formatted data into a single output file
formatted_data.to_csv('formatted_sales_data.csv', index=False)
