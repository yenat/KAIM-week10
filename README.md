# Time Series Analysis and Impact Study on Brent Oil Prices

## Project Overview

This project focuses on the analysis of Brent Oil Prices over time, assessing the impact of significant events on oil prices, and performing time series modeling using ARIMA and GARCH models. The study includes data visualization, descriptive statistics, impact analysis, and time series modeling to gain insights into the behavior of Brent oil prices.

## Data Sources

The analysis uses three main data sources:
1. **Brent Oil Prices**
2. **Economic Indicators (GDP Growth)**
3. **Stock Market Trends (S&P 500 Index)**

## Analysis Steps

### 1. Data Merging

The data from the three sources were merged based on the date column, ensuring that all dates are included and missing values are filled using backward filling.

### 2. Exploratory Data Analysis (EDA)

#### 2.1 Visualize Data
Time series plots were created for Brent oil prices, GDP growth, and S&P 500 index to visualize trends, seasonality, and anomalies.

#### 2.2 Descriptive Statistics
Summary statistics (mean, median, standard deviation) were computed to understand the distribution of prices.

#### 2.3 Event Annotation
Significant events that could impact oil prices were identified and annotated on the time series plot. Example events include:
- **Lehman Brothers Bankruptcy** (2008-09-15)
- **WHO Declares COVID-19 a Pandemic** (2020-03-11)
- **Russia Invades Ukraine** (2022-02-24)

### 3. Time Series Analysis

#### 3.1 Model Selection: ARIMA
The ARIMA (AutoRegressive Integrated Moving Average) model was selected and fitted to the Brent oil prices data. The model order was determined using AIC (Akaike Information Criterion) and BIC (Bayesian Information Criterion).

#### 3.2 Model Fitting: ARIMA
The ARIMA model was fitted to the data, and the performance was assessed using RMSE (Root Mean Squared Error).

#### 3.3 Model Selection: GARCH
The GARCH (Generalized Autoregressive Conditional Heteroskedasticity) model was selected to capture volatility clustering in the residuals of the ARIMA model.

#### 3.4 Model Fitting: GARCH
The GARCH model was fitted to the residuals of the ARIMA model, and the performance was assessed using AIC and BIC.

### 4. Impact Analysis

#### 4.1 Quantify Impact
Statistical tests (t-test) were used to measure the impact of identified events on Brent oil prices.

#### 4.2 Pre-Post Event Analysis
Price changes before, during, and after significant events were analyzed to quantify their effects.

### 5. Insights and Reporting

Key findings from the impact analysis and time series modeling were summarized to provide clear and concise insights.

## Key Findings

- Significant events such as the Lehman Brothers Bankruptcy, COVID-19 pandemic declaration, and Russia-Ukraine conflict had noticeable impacts on Brent oil prices.
- The ARIMA model effectively captured the trend in oil prices, while the GARCH model captured the volatility clustering.
- Pre-post event analysis revealed substantial percentage changes in oil prices during significant events.

## Conclusion

This project provides a comprehensive analysis of Brent oil prices, leveraging time series modeling and impact analysis to understand the effects of significant events. The findings offer valuable insights into the behavior of oil prices and can inform future research and decision-making.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yenat/KAIM-week10.git
   cd KAIM-week10
   pip install -r requirements.txt
   python app.py
   python dashboard.py
   ```
   Open a web browser and navigate to http://127.0.0.1:5002 to view the dashboard.

2. For further analysis:
   ``` bash
   
    cd KAIM-week89
    jupyter notebook notebooks/EDA.ipynb
    jupyter notebook notebooks/time_series_analysis.ipynb
    jupyter notebook notebooks/impact_analysis.ipynb
    jupyter notebook notebooks/task2_analysis.ipynb

    ```



