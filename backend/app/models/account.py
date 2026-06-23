from sqlalchemy import (
    Column,
    String,
    Numeric,
    ForeignKey,
    DateTime
)
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from backend.app.database.base import Base

class Account(Base):
    __tablename__ = "accounts"

    account_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    customer_id = Column(
        UUID(as_uuid=True),
        ForeignKey("customers.customer_id")
    )

    account_number = Column(
        String,
        unique=True,
        nullable=False
    )

    account_type = Column(String)

    balance = Column(
        Numeric(18,2),
        default=0
    )

    status = Column(
        String,
        default="ACTIVE"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )