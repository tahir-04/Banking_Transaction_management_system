import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime

from backend.app.database.base import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    audit_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    customer_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "customers.customer_id"
        )
    )

    action = Column(String)

    details = Column(JSONB)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )