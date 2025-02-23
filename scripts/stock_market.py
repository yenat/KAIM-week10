import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

# Define date range
start_date = '1987-05-20'
end_date = '2022-11-14'

# Define the FRED GDP growth indicator
fred_indicator = 'SP500'

# Retrieve data from FRED
data = web.DataReader(fred_indicator, 'fred', start_date, end_date)

# Generate all dates in the specified range
date_range = pd.date_range(start=start_date, end=end_date, freq='B')  # 'B' for business days

# Create a DataFrame with the specific dates
specific_dates_df = pd.DataFrame({'Date': date_range})
specific_dates_df['Date'] = specific_dates_df['Date'].dt.strftime('%d-%b-%y')

# Reset index and process data
data.reset_index(inplace=True)
data['DATE'] = pd.to_datetime(data['DATE']).dt.strftime('%d-%b-%y')
data.columns = ['Date', 'sp500']

# Merge the data with the specific dates to include all the specified dates
merged_data = pd.merge(specific_dates_df, data, on='Date', how='left')

# Forward-fill the missing values to ensure continuity
merged_data = merged_data.fillna(method='ffill')

# Save to CSV
merged_data.to_csv('stock_market_trends.csv', index=False)
print("Data successfully retrieved and saved to stock_market_trends.csv")
