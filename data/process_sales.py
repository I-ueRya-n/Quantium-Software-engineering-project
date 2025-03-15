import pandas as pd
import os

# Get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the absolute path of the data folder
data_folder = os.path.join(script_dir)

# List of input CSV files
files = [
    os.path.join(data_folder, 'daily_sales_data_0.csv'),
    os.path.join(data_folder, 'daily_sales_data_1.csv'),
    os.path.join(data_folder, 'daily_sales_data_2.csv')
]

processed_data = []

for file in files:
    # Read each CSV file
    df = pd.read_csv(file)
    
    # Filter rows for 'pink morsel' (case-sensitive match)
    df = df[df['product'] == 'pink morsel']
    
    # Remove '$' from price and convert to float
    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
    
    # Calculate sales (quantity * price)
    df['sales'] = df['quantity'] * df['price']
    
    # Keep only the required columns
    df = df[['sales', 'date', 'region']]
    df['sales'] = df['sales'].apply(lambda x: f"${x:.2f}")
    
    processed_data.append(df)

# Combine all processed data
final_df = pd.concat(processed_data, ignore_index=True)

# Define the output file path inside the same data folder
output_file = os.path.join(data_folder, 'formatted_sales_data.csv')

# Save to formatted_sales_data.csv
final_df.to_csv(output_file, index=False)

# Print confirmation message
print(f"Formatted data saved to {output_file}")
