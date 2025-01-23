# Financial Statement Analyst

## Overview
Financial Statement Analyst is a FastAPI-based project that provides a platform to Large Language Models (LLMs) like GPT-4 to analyze financial data and predict future earnings trends. The project integrates financial data processing with advanced AI-powered predictions to deliver actionable insights. The implementation is inspired by the working paper "Financial Statement Analysis with Large Language Models" from the Becker Friedman Institute ([Paper](https://bfi.uchicago.edu/wp-content/uploads/2024/05/BFI_WP_2024-65.pdf)).


---

## Features
- Fetch financial data(like annual balance sheet, income statement and cash flow) for companies using a reliable API.
- Process and clean financial data into standardized formats.
- Calculate key financial ratios and metrics for balance sheets, income statements, and cash flow statements.
- Leverage OpenAI's GPT models for financial analysis and predictions.
- Chain-of-Thought (CoT) Prompt: Guide the model step-by-step:
    - Identify trends in financial line items.
    - Compute key financial ratios (e.g., profitability, liquidity, leverage).
    - Generate a narrative interpretation of the ratios.
    - Predict whether earnings will increase or decrease in the next period.
- Generate and export financial analysis reports.
- RESTful API endpoints for seamless integration with other tools.
---
# Financial Ratios Overview

## 1. Balance Sheet Ratios (`calculate_financial_ratios`)
These ratios assess liquidity and leverage using balance sheet data:

### Current Ratio
**Formula:**
```
total_current_assets / total_current_liabilities
```
**Purpose:** Measures short-term liquidity (ability to cover current liabilities with current assets).

### Quick Ratio
**Formula:**
```
(cash + short_term_investments + receivables) / total_current_liabilities
```
**Purpose:** A stricter liquidity metric excluding inventory.

### Debt-to-Equity Ratio
**Formula:**
```
total_liabilities / total_stockholders_equity
```
**Purpose:** Indicates leverage by comparing debt to shareholders' equity.

### Debt Ratio
**Formula:**
```
total_liabilities / total_assets
```
**Purpose:** Shows the proportion of assets financed by debt.

### Net Debt-to-Equity Ratio
**Formula:**
```
(total_debt - cash) / total_stockholders_equity
```
**Purpose:** Adjusts debt for cash holdings to reflect true leverage.

### Equity Ratio
**Formula:**
```
total_stockholders_equity / total_assets
```
**Purpose:** Highlights equity funding proportion in total assets.

---

## 2. Income Statement Ratios (`calculate_income_statement_ratios`)
These ratios evaluate profitability and earnings performance:

### Margins
#### Gross Profit Margin
**Formula:**
```
gross_profit / revenue
```
#### Operating Profit Margin
**Formula:**
```
operating_income / revenue
```
#### Net Profit Margin
**Formula:**
```
net_income / revenue
```
#### EBITDA Margin
**Formula:**
```
ebitda / revenue
```
**Purpose:** All margins measure profitability at different stages of operations.

### Earnings Per Share (EPS)
#### Basic EPS
**Formula:**
```
net_income / weighted_average_shs_out
```
#### Diluted EPS
**Formula:**
```
net_income / weighted_average_shs_out_dil
```
**Purpose:** Reflects profitability per share, accounting for potential dilution.

---

## 3. Cash Flow Metrics (`calculate_cash_flow_metrics`)
These metrics analyze cash generation and usage:

### Operating Cash Flow Ratio
**Formula:**
```
operating_cash_flow / total_liabilities
```
**Purpose:** Assesses ability to cover liabilities with operating cash flow.

### Cash Flow Margin
**Formula:**
```
operating_cash_flow / revenue
```
**Purpose:** Measures cash efficiency relative to revenue.

### Reinvestment Ratio
**Formula:**
```
capital_expenditures / operating_cash_flow
```
**Purpose:** Shows reinvestment intensity in fixed assets.

### Dividend Payout Ratio
**Formula:**
```
dividends_paid / free_cash_flow
```
**Purpose:** Indicates dividends paid as a percentage of free cash flow.

### FCF-to-Revenue
**Formula:**
```
free_cash_flow / revenue
```
**Purpose:** Free cash flow generated per revenue unit.

### Cash Conversion Efficiency
**Formula:**
```
operating_cash_flow / net_income
```
**Purpose:** Measures how efficiently net income converts to cash.

---
## Technologies Used
- **FastAPI**: For building the RESTful API.
- **Python**: Core programming language.
- **Pandas**: Data processing and manipulation.
- **Requests**: Fetching data from external APIs.
- **OpenAI API**: Integrating AI for financial analysis.
- **HTML, CSS, JavaScript**: Web-based UI.
---
## Installation

### Prerequisites
1. Python 3.8+
2. Git
3. OpenAI API Key

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/utkarshx27/llm-financial-statement-analyst.git
    cd llm-financial-statement-analyst
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set environment variables for OpenAI API Key:
    ```bash
    export OPENAI_API_KEY="your_openai_api_key"
    ```

---

## Usage

### Running the API
1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).


## Web Interface
The project now features an interactive web-based UI for financial analysis:

- Visit the homepage of the application.
- Select a ticker symbol from the dropdown menu (e.g., AAPL, MSFT, GOOG).
- Click "Generate Analysis" to fetch, process, and analyze the company's financial data.
- View the AI-generated insights, including financial trends, ratios, and predictions for earnings.

---
## Example:
![Alt Text](https://raw.githubusercontent.com/utkarshx27/llm-financial-statement-analyst/main/example/1.png)
![Alt Text](https://raw.githubusercontent.com/utkarshx27/llm-financial-statement-analyst/main/example/2.png)
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



```

