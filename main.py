import csv
 
# File paths for the input and output CSV files
input_files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
output_file = 'output/soul_food_sales.csv'
 
# Create a list to store the processed rows
processed_rows = []
 
# Read and process each input CSV file
for file_path in input_files:
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        # Process each row in the current CSV file
        for row in reader:
            # Only keep the rows where product is 'Pink Morsels'
            if row['product'] == 'pink morsel':
                price = float(row['price'].replace('$','').strip())
                quantity =  float(row['quantity'])
                # Calculate sales as quantity * price
                sales = price * quantity
                
                # Create a new row with the required fields
                processed_row = {
                    'sales': sales,
                    'date': row['date'],
                    'region': row['region']
                }
                processed_rows.append(processed_row)
 
# Write the processed data into the output CSV file
with open(output_file, mode='w', newline='') as file:
    fieldnames = ['sales', 'date', 'region']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write the data rows
    writer.writerows(processed_rows)
 
print(f"File has been processed and saved as '{output_file}'")