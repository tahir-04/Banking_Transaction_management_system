from pydantic import BaseModel
from pydantic import EmailStr

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    password: str