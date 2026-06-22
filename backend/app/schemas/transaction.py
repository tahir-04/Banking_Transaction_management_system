from pydantic import BaseModel
from decimal import Decimal

class TransferRequest(BaseModel):
    receiver_account: str
    amount: Decimal