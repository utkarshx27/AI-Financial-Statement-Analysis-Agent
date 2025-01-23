from pydantic import BaseModel


class FinancialDataRequest(BaseModel):
    ticker: str 
