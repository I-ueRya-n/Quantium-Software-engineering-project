import os
import csv

FILE_PATH = './data'
OUTPUT_FILE_PATH = './formatted_data.csv'

#open the file 

with open (OUTPUT_FILE_PATH, 'w') as output_file:
    writer = csv.writer(output_file)

    # add csv header
    header = ['sales', 'date', 'region']
    writer.writerow(header)

    # Go through all the file in the directory
    for file_name in os.listdir(FILE_PATH):
        # open the csv file for reading
        with open (f"{FILE_PATH}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
        # iterate through each row in the csv file
            row_index = 0
            for input_row in reader:
                if row_index > 0:
                     if len(input_row) >= 5:
                        product = input_row[0]
                        raw_price = input_row[1]
                        quantity = input_row[2]
                        deal_date = input_row[3]
                        region = input_row[4]

                # data filt if the product is pink morsel
                        if  product == 'pink morsel':
                            price = float (raw_price[1:])
                            sales = price * int(quantity) 


                            output_row = [sales, deal_date, region]
                            writer.writerow(output_row)
                row_index += 1

