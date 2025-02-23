import pandas as pd

# Load the CSV files into DataFrames
brent_data = pd.read_csv('BrentOilPrices.csv')
economic_data = pd.read_csv('economic_indicators.csv')
stock_data = pd.read_csv('stock_market_trends.csv')

# Convert the 'Date' columns to datetime format for merging, automatically inferring the format
brent_data['Date'] = pd.to_datetime(brent_data['Date'], infer_datetime_format=True)
economic_data['Date'] = pd.to_datetime(economic_data['Date'], infer_datetime_format=True)
stock_data['Date'] = pd.to_datetime(stock_data['Date'], infer_datetime_format=True)

# Merge the DataFrames on the 'Date' column
merged_data = pd.merge(brent_data, economic_data, on='Date', how='outer')
merged_data = pd.merge(merged_data, stock_data, on='Date', how='outer')

# Sort the merged DataFrame by 'Date'
merged_data = merged_data.sort_values('Date')

# Backward-fill the missing values to ensure continuity
merged_data = merged_data.bfill()

# Save the merged DataFrame to a new CSV file
merged_data.to_csv('merged_data.csv', index=False)

print("Data successfully merged and saved to merged_data.csv")
