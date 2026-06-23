from pydantic import BaseModel
from decimal import Decimal


class CreateAccountRequest(BaseModel):
    account_type: str


class DepositRequest(BaseModel):
    account_number: str
    amount: Decimal


class WithdrawRequest(BaseModel):
    account_number: str
    amount: Decimal


class TransferRequest(BaseModel):
    sender_account: str
    receiver_account: str
    amount: Decimal

class DepositRequest(BaseModel):
    account_number: str
    amount: Decimal