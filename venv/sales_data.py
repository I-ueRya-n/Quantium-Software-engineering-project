import pandas as pd
df1 = pd.read_csv('../data/daily_sales_data_0.csv')
df2 = pd.read_csv('../data/daily_sales_data_1.csv')
df3 = pd.read_csv('../data/daily_sales_data_2.csv')

combined_df = pd.concat([df1, df2, df3])
combined_df = combined_df[combined_df["product"] == 'pink morsel']
combined_df['sales'] = combined_df.iloc[:,1].str.replace('$','').astype('float64') * combined_df.iloc[:, 2]
combined_df = combined_df.drop(columns=[combined_df.columns[1], combined_df.columns[2]])
combined_df = combined_df.reindex(columns=['sales', 'date', 'region'])
combined_df.to_csv('../managed_data.csv', index=False)