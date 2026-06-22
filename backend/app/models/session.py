import uuid
from sqlalchemy import Column, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID

from backend.app.database.base import Base


class Session(Base):
    __tablename__ = "sessions"

    session_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    customer_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )

    refresh_token = Column(
        Text,
        nullable=False
    )

    expires_at = Column(
        DateTime,
        nullable=False
    )