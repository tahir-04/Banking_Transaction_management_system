from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from backend.app.database.base import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    first_name = Column(String)
    last_name = Column(String)

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    phone = Column(
        String,
        unique=True
    )

    password_hash = Column(String)

    role = Column(
        String,
        default="CUSTOMER"
    )

    is_verified = Column(
        Boolean,
        default=False
    )