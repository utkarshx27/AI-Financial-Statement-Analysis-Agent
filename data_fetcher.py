import os
import requests
import pandas as pd


# fitching financial data
# https://site.financialmodelingprep.com/developer/docs#income-statements-financial-statements


def get_financial_data(ticker, data_type):
    base_url = 'https://financialmodelingprep.com/api'
    api_key = "financialmodelingprep API KEY"
    url = f'{base_url}/v3/{data_type}/{ticker}?period=annual&apikey={api_key}'

    try:
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}")

        data = response.json()

        if not data or 'error' in data:
            raise ValueError(f"No data found for ticker {ticker} or the API returned an error: {data.get('error', 'Unknown error')}")

        df = pd.DataFrame(data)

        try:
            df.to_csv(f'{ticker}_{data_type}_data.csv', index=False)
        except Exception as e:
            raise Exception(f"Error saving data to CSV: {e}")

        return df

    except requests.exceptions.RequestException as e:
        print(f"Request exception occurred: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None