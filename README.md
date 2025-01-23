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

