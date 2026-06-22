from pydantic import BaseModel

class AccountCreate(BaseModel):
    account_type: str