import os
import requests
import pandas as pd

def calculate_financial_ratios(df):
    dfc = df.copy()

    dfc['current_ratio'] = dfc['totalcurrentassets'] / dfc['totalcurrentliabilities']
    dfc['quick_ratio'] = (dfc['cashandcashequivalents'] + dfc['shortterminvestments'] + dfc['netreceivables']) / dfc['totalcurrentliabilities']

    dfc['debt_to_equity_ratio'] = dfc['totalliabilities'] / dfc['totalstockholdersequity']
    dfc['debt_ratio'] = dfc['totalliabilities'] / dfc['totalassets']
    dfc['net_debt_to_equity_ratio'] = (dfc['totaldebt'] - dfc['cashandcashequivalents']) / dfc['totalstockholdersequity']

    dfc['equity_ratio'] = dfc['totalstockholdersequity'] / dfc['totalassets']
    return dfc


def calculate_income_statement_ratios(df):
    dfc = df.copy()

    dfc['gross_profit_margin'] = dfc['grossprofit'] / dfc['revenue']
    dfc['operating_profit_margin'] = dfc['operatingincome'] / dfc['revenue']
    dfc['net_profit_margin'] = dfc['netincome'] / dfc['revenue']
    dfc['ebitda_margin'] = dfc['ebitda'] / dfc['revenue']

    dfc['eps'] = dfc['netincome'] / dfc['weightedaverageshsout']
    dfc['eps_diluted'] = dfc['netincome'] / dfc['weightedaverageshsoutdil']

    return dfc


def calculate_cash_flow_metrics(cash_flow_df, income_df=None, balance_df=None):
    df = cash_flow_df.copy()

    required_columns = ['netcashprovidedbyoperatingactivities', 'freecashflow',
                        'dividendspaid', 'netincome', 'investmentsinpropertyplantandequipment']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Missing necessary columns in cash flow data")

    if balance_df is not None:
        total_liabilities = balance_df['totalliabilities'].iloc[0]
        df['operating_cash_flow_ratio'] = df['netcashprovidedbyoperatingactivities'] / total_liabilities

    if income_df is not None:
        revenue = income_df['revenue'].iloc[0]
        df['cash_flow_margin'] = df['netcashprovidedbyoperatingactivities'] / revenue

    df['reinvestment_ratio'] = df['investmentsinpropertyplantandequipment'] / df['netcashprovidedbyoperatingactivities']

    df['dividend_payout_ratio'] = df['dividendspaid'] / df['freecashflow']

    if income_df is not None:
        df['fcf_to_revenue'] = df['freecashflow'] / revenue

    df['cash_conversion_efficiency'] = df['netcashprovidedbyoperatingactivities'] / df['netincome']

    return df