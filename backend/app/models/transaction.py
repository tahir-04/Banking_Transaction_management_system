import uuid
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from backend.app.database.base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    sender_account = Column(
        UUID(as_uuid=True)
    )

    receiver_account = Column(
        UUID(as_uuid=True)
    )

    amount = Column(
        Numeric(18, 2)
    )

    transaction_type = Column(String)

    reference_number = Column(
        String,
        unique=True
    )

    status = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )