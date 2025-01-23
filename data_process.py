import os
import requests
import pandas as pd

def std_financial_data(df):
    if df is None or df.empty:
        raise ValueError("Input DataFrame is empty or None.")
    dfc = df.copy()

    if 'calendarYear' not in dfc.columns:
        raise KeyError("'calendarYear' column is missing from the input DataFrame.")

    dfc['calendarYear'] = pd.to_numeric(dfc['calendarYear'], errors='coerce')

    if dfc['calendarYear'].isna().any():
        raise ValueError("There are invalid or missing values in 'calendarYear' after conversion.")

    current_year = dfc['calendarYear'].max()

    if pd.isna(current_year) or current_year < 1900:
        raise ValueError(f"Invalid current year: {current_year} found in 'calendarYear'.")

    dfc['calendarYear'] = dfc['calendarYear'].apply(
        lambda x: f"t-{current_year - x}" if x < current_year else "t"
    )

    columns_to_remove = ['cik', 'symbol', 'fillingDate', 'acceptedDate', 'calendarYear', 'link', 'finalLink']
    missing_columns = [col for col in columns_to_remove if col not in dfc.columns]

    if missing_columns:
        raise KeyError(f"The following columns are missing from the DataFrame: {', '.join(missing_columns)}")

    dfc = dfc.drop(columns=columns_to_remove)

    dfc.columns = dfc.columns.str.lower().str.replace(' ', '_')

    return dfc



