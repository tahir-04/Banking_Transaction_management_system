import uuid
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy.dialects.postgresql import UUID
from backend.app.database.base import Base

class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    customer_id = Column(
        UUID(as_uuid=True)
    )

    account_number = Column(
        String,
        unique=True
    )

    account_type = Column(String)

    balance = Column(
        Numeric(18, 2),
        default=0
    )

    status = Column(
        String,
        default="ACTIVE"
    )