from pydantic import BaseModel

class FinancialDataRequest(BaseModel):
    ticker: str
    data_type: str

