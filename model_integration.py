import os
import requests
import pandas as pd
import openai
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")


def financial_analysis_cot(model, balance_sheet, income_statement, cash_flow):
    prompt = (
        "You are a financial analyst. Analyze the following financial data step-by-step to predict whether earnings will increase or decrease in the next period. Follow these steps:\n"
        "1. Identify key trends in the financial line items provided.\n"
        "2. Compute key financial ratios, including profitability, liquidity, leverage, and efficiency ratios.\n"
        "3. Provide a narrative interpretation of the computed ratios, focusing on their implications for financial performance.\n"
        "4. Based on the trends and ratio analysis, predict whether earnings will increase or decrease in the next period, and explain your reasoning clearly.\n"
        f"Balance Sheet:\n{balance_sheet}\n\n"
        f"Income Statement:\n{income_statement}\n\n"
        f"Cash Flow:\n{cash_flow}\n\n"
    )

    client = OpenAI()

    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "user", "content": prompt}
        ],
        top_p=1
    )

    result = response.choices[0].message.content

    return {
        "analysis": result
    }