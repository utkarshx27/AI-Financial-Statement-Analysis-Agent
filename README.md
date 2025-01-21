# Financial Statement Analysis with gpt-4o


This repository implements financial statement analysis using Large Language Models (LLMs) like GPT-4 to analyze financial data and predict future earnings trends. The implementation is inspired by the working paper "Financial Statement Analysis with Large Language Models" from the Becker Friedman Institute ([Paper](https://bfi.uchicago.edu/wp-content/uploads/2024/05/BFI_WP_2024-65.pdf)).

---

## Features

1. **Data Fetching:**
   - Fetch balance sheet, income statement, and cash flow statement data from the Financial Modeling Prep API.
   
2. **Data Processing:**
   - Standardizes and preprocesses financial data by normalizing column names and creating time-based indices (e.g., `t`, `t-1`).

3. **Financial Ratio Calculation:**
   - Computes key financial ratios for liquidity, leverage, profitability, and efficiency.

4. **LLM Integration:**
   - Converts processed financial data into textual format.
   - Uses a Chain-of-Thought (CoT) prompting technique to guide the LLM in analyzing trends and predicting earnings changes.

5. **End-to-End Pipeline:**
   - Combines data fetching, processing, and LLM analysis into a streamlined process.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/financial-statement-analysis-llm.git
   cd financial-statement-analysis-llm
   ```

2. Install dependencies:

   ```bash
   import requests
   import pandas as pd
   import os
   from openai import OpenAI
   ```

3. Set up API keys:
   - Financial Modeling Prep API Key: Obtain from [Financial Modeling Prep](https://site.financialmodelingprep.com/developer/docs).
   - OpenAI API Key: Obtain from [OpenAI](https://platform.openai.com/).

   Add your API keys to a secure storage method or hardcode them in the script (not recommended).

---

## Usage

### 1. Data Fetching
Fetch financial data for a given ticker:

```python
balance_sheet = get_financial_data('AAPL', 'balance-sheet-statement')
income_statement = get_financial_data('AAPL', 'income-statement')
cash_flow = get_financial_data('AAPL', 'cash-flow-statement')
```

### 2. Data Preprocessing
Standardize the financial data:

```python
balance_sheet_processed = std_financial_data(balance_sheet)
income_statement_processed = std_financial_data(income_statement)
cash_flow_processed = std_financial_data(cash_flow)
```

### 3. Ratio Calculation

```python
balance_sheet_with_ratios = calculate_financial_ratios(balance_sheet_processed)
income_statement_with_ratios = calculate_income_statement_ratios(income_statement_processed)
cash_flow_with_metrics = calculate_cash_flow_metrics(cash_flow_processed, income_statement_processed, balance_sheet_processed)
```

### 4. LLM Analysis
Prepare and analyze the financial data using the LLM:

```python
balance_sheet_string = convert_to_string(balance_sheet_with_ratios)
income_statement_string = convert_to_string(income_statement_with_ratios)
cash_flow_string = convert_to_string(cash_flow_with_metrics)

result = financial_analysis_cot(
    model='gpt-4',
    balance_sheet=balance_sheet_string,
    income_statement=income_statement_string,
    cash_flow=cash_flow_string
)

print("Analysis:", result["analysis"])
```

---

## File Structure

- `main.py`: Contains the primary code for data fetching, processing, and analysis.
- `requirements.txt`: List of dependencies.
- `README.md`: This file.

---

## Example Output

**Prediction:**
> Analysis: To predict whether earnings will increase or decrease in the next period, we will follow the outlined steps:

### Step 1: Identify Key Trends in Financial Line Items

1. **Revenue and Gross Profit**: Revenue has shown a fluctuating trend, with a slight decrease from 2022 to 2023, followed by an increase in 2024. Gross profit has increased in 2024 compared to 2023, indicating improved cost management or pricing strategies.

2. **Operating Income and Net Income**: Both operating income and net income have increased in 2024 compared to 2023, suggesting improved operational efficiency and profitability.

3. **Cash and Short-term Investments**: There is a significant increase in cash and short-term investments from 2023 to 2024, indicating improved liquidity.

4. **Total Debt**: Total debt has decreased from 2023 to 2024, which may reduce interest expenses and improve net income.

5. **Equity**: Total stockholders' equity has decreased slightly from 2023 to 2024, which could be due to share repurchases or dividend payments.

### Step 2: Compute Key Financial Ratios

1. **Profitability Ratios**:
   - **Gross Profit Margin**: 2024: 46.21%, 2023: 44.13%
   - **Operating Profit Margin**: 2024: 31.51%, 2023: 29.82%
   - **Net Profit Margin**: 2024: 23.97%, 2023: 25.31%

2. **Liquidity Ratios**:
   - **Current Ratio**: 2024: 0.87, 2023: 0.99
   - **Quick Ratio**: 2024: 0.75, 2023: 0.84

3. **Leverage Ratios**:
   - **Debt to Equity Ratio**: 2024: 5.41, 2023: 4.67
   - **Debt Ratio**: 2024: 0.84, 2023: 0.82

4. **Efficiency Ratios**:
   - **Operating Cash Flow Ratio**: 2024: 0.38, 2023: 0.36

### Step 3: Narrative Interpretation of Ratios

- **Profitability**: The increase in gross and operating profit margins in 2024 indicates better cost control and operational efficiency. However, the slight decrease in net profit margin suggests increased expenses or lower other income.

- **Liquidity**: The decline in both current and quick ratios from 2023 to 2024 indicates a potential decrease in short-term liquidity, which could be a concern if the trend continues.

- **Leverage**: The increase in the debt to equity ratio suggests higher financial leverage, which could increase financial risk. However, the decrease in total debt is a positive sign.

- **Efficiency**: The operating cash flow ratio has improved, indicating better cash generation from operations relative to liabilities.

### Step 4: Predict Earnings Trend

Based on the analysis:

- **Positive Indicators**: Increased revenue, gross profit, and operating income in 2024 suggest a strong operational performance. The decrease in total debt and improved cash flow efficiency are also positive signs.

- **Negative Indicators**: The decrease in liquidity ratios and net profit margin could pose challenges if not addressed.

**Prediction**: Earnings are likely to **increase** in the next period, driven by improved operational efficiency and cost management. However, the company should monitor liquidity and leverage to ensure sustainable growth.

---

## Contribution Guidelines

1. Fork the repository and create a new branch for your feature or bug fix.
2. Submit a pull request with a clear description of your changes.
3. Ensure your code adheres to PEP 8 standards.

---

## References

- [Financial Modeling Prep API Documentation](https://site.financialmodelingprep.com/developer/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Financial Statement Analysis with Large Language Models](https://bfi.uchicago.edu/wp-content/uploads/2024/05/BFI_WP_2024-65.pdf)

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

