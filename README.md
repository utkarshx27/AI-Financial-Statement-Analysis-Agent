# Financial Statement Analyst

## Overview
Financial Statement Analyst is a FastAPI-based project that provides a platform to Large Language Models (LLMs) like GPT-4 to analyze financial data and predict future earnings trends. The project integrates financial data processing with advanced AI-powered predictions to deliver actionable insights. The implementation is inspired by the working paper "Financial Statement Analysis with Large Language Models" from the Becker Friedman Institute ([Paper](https://bfi.uchicago.edu/wp-content/uploads/2024/05/BFI_WP_2024-65.pdf)).


---

## Features
- Fetch financial data for companies using a reliable API.
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
## Technologies Used
- **FastAPI**: For building the RESTful API.
- **Python**: Core programming language.
- **Pandas**: Data processing and manipulation.
- **Requests**: Fetching data from external APIs.
- **OpenAI API**: Integrating AI for financial analysis.
- **cURL**: Testing API endpoints.
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
    fastapi dev main.py
    uvicorn main:app --reload
    ```

2. The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).


### API Endpoints

#### `POST /fetch-process-analyze`
Fetch, process, and analyze financial data for a given ticker.

**Request Body:**
```json
{
  "ticker": "AAPL",
  "data_type": "balance-sheet-statement"
}
```

**Response:**
```json
{
  "analysis": "AI-generated financial insights",
  "log_probs": "Log probabilities from OpenAI API"
}
```

### Testing the API with `cURL`
```bash
curl -X POST "http://127.0.0.1:8000/fetch-process-analyze" ^
-H "Content-Type: application/json" ^
-d "{\"ticker\": \"AAPL\", \"data_type\": \"balance-sheet-statement\"}"
```

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

