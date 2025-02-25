import pandas as pd
import requests
from io import BytesIO

# URLs for the datasets
gdp_url = 'http://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv'
inflation_url = 'https://www.imf.org/external/datamapper/PCPIPCH@WEO/OEMDC/ADVEC/WEOWORLD'
unemployment_url = 'http://api.worldbank.org/v2/en/indicator/SL.UEM.TOTL.NE.ZS?downloadformat=csv'
exchange_rate_url = 'https://www.imf.org/external/np/fin/data/param_rms_mth.aspx'

# Function to download and save CSV files
def download_csv(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Data downloaded and saved to {filename}")

# Download data
download_csv(gdp_url, 'gdp_data.zip')
download_csv(unemployment_url, 'unemployment_data.zip')


import pandas as pd

# Load datasets
gdp_data = pd.read_csv('../scripts/gdp_data.csv', skiprows=4)
unemployment_data = pd.read_csv('../scripts/unemployment_data.csv', skiprows=4)
brent_oil_data = pd.read_csv('../scripts/BrentOilPrices.csv')


# Function to reshape the data
def reshape_data(df, id_vars, value_vars, var_name, value_name):
    df_long = pd.melt(df, id_vars=id_vars, value_vars=value_vars, 
                      var_name=var_name, value_name=value_name)
    return df_long

# Reshape GDP data
gdp_long = reshape_data(gdp_data, id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
                        value_vars=gdp_data.columns[4:], var_name='Year', value_name='GDP')

# Reshape Unemployment data
unemployment_long = reshape_data(unemployment_data, id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
                                 value_vars=unemployment_data.columns[4:], var_name='Year', value_name='Unemployment Rate')

# Filter for a specific country, e.g., United States
gdp_long = gdp_long[gdp_long['Country Name'] == 'United States']
unemployment_long = unemployment_long[unemployment_long['Country Name'] == 'United States']

# Convert Year to datetime format and extract the year
gdp_long['Year'] = pd.to_datetime(gdp_long['Year'], format='%Y', errors='coerce').dt.year
unemployment_long['Year'] = pd.to_datetime(unemployment_long['Year'], format='%Y', errors='coerce').dt.year

# Merge the GDP and Unemployment data
merged_data = pd.merge(gdp_long, unemployment_long, on=['Country Name', 'Year'], suffixes=('_GDP', '_Unemployment'))

# Convert Brent Oil Prices 'Date' to datetime format and extract the year
brent_oil_data['Date'] = pd.to_datetime(brent_oil_data['Date'], format='%d-%b-%y', errors='coerce')
brent_oil_data['Year'] = brent_oil_data['Date'].dt.year

# Merge all datasets on the 'Year'
final_merged_data = pd.merge(brent_oil_data, merged_data, left_on='Year', right_on='Year')

# Save the final merged dataset
final_merged_data.to_csv('final_merged_data.csv', index=False)
print("Data merging complete. Merged data saved to final_merged_data.csv")