import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

# Define date range
start_date = datetime.strptime('1987-05-20', '%Y-%m-%d')
end_date = datetime.strptime('2022-11-14', '%Y-%m-%d')

# Generate all dates in the specified range
date_range = pd.date_range(start_date, end_date, freq='B')  # 'B' for business days

# Create a DataFrame with the specific dates
specific_dates_df = pd.DataFrame({'Date': date_range})
specific_dates_df['Date'] = specific_dates_df['Date'].dt.strftime('%d-%b-%y')

# Define the FRED GDP growth indicator
fred_indicator = 'GDP'

# Retrieve data from FRED
data = web.DataReader(fred_indicator, 'fred', start_date, end_date)

# Reset index and process data
data.reset_index(inplace=True)
data['DATE'] = pd.to_datetime(data['DATE']).dt.strftime('%d-%b-%y')
data.columns = ['Date', 'gdp_growth']

# Merge the data with the specific dates to include all the specified dates
merged_data = pd.merge(specific_dates_df, data, on='Date', how='left')

# Forward-fill the GDP growth values to match each date
merged_data['gdp_growth'] = merged_data['gdp_growth'].fillna(method='ffill')

# Save to CSV
merged_data.to_csv('economic_indicators.csv', index=False)
