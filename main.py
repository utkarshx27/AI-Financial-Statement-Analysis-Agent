from fastapi import FastAPI, HTTPException
from data_fetcher import get_financial_data     # Fetching financial data
from data_process import std_financial_data     # Standardizing financial data
from ratios_calculator import (                 
    calculate_financial_ratios,                 # Calculating financial ratios for balance sheet
    calculate_income_statement_ratios,          # Calculating financial ratios for income statement
    calculate_cash_flow_metrics,                # Calculating financial metrics for cash flow
)
from convert_to_string import convert_to_string # Converting DataFrames to strings
from model_integration import financial_analysis_cot # Integrating model with financial data
from schemas import FinancialDataRequest
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)






@app.post("/fetch-process-analyze")
def process_financial_data_endpoint(request: FinancialDataRequest):
    """
    Fetch, process, and analyze financial data for the given ticker.
    ---
    Input:
      - ticker: Stock ticker symbol (e.g., 'AAPL').
    Output:
      - Analysis and predictions based on financial data.
    """
    try:
        # Step 1: Fetch raw datasets
        balance_sheet = get_financial_data(request.ticker, "balance-sheet-statement")
        income_statement = get_financial_data(request.ticker, "income-statement")
        cash_flow = get_financial_data(request.ticker, "cash-flow-statement")
        print("Data fetched successfully")

        # Step 2: Standardize datasets
        balance_sheet_processed = std_financial_data(balance_sheet)
        income_statement_processed = std_financial_data(income_statement)
        cash_flow_processed = std_financial_data(cash_flow)
        print("Data processed successfully")

        # Step 3: Calculate financial ratios and metrics
        balance_sheet_with_ratios = calculate_financial_ratios(balance_sheet_processed)
        income_statement_with_ratios = calculate_income_statement_ratios(income_statement_processed)
        cash_flow_with_metrics = calculate_cash_flow_metrics(
            cash_flow_processed,
            income_statement_processed,
            balance_sheet_processed,
        )
        print("Ratios and metrics calculated successfully")

        # Step 4: Convert DataFrames to strings for analysis
        income_statement_string = convert_to_string(income_statement_with_ratios)
        balance_sheet_string = convert_to_string(balance_sheet_with_ratios)
        cash_flow_string = convert_to_string(cash_flow_with_metrics)
        print("Data converted to strings successfully")

        # Step 5: Generate financial analysis using OpenAI
        result = financial_analysis_cot(
            model="gpt-4o",
            balance_sheet=balance_sheet_string,
            income_statement=income_statement_string,
            cash_flow=cash_flow_string,
        )
        print("Financial analysis generated successfully")
        
        # Step 6: Return analysis results
        return {
            "analysis": result.get("analysis"),
            #"log_probs": result.get("log_probs"),
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Value Error: {ve}")
    except KeyError as ke:
        raise HTTPException(status_code=400, detail=f"Key Error: {ke}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected Error: {e}")


# Serve static files (HTML/CSS/JS)
app.mount("/", StaticFiles(directory="static", html=True), name="static")