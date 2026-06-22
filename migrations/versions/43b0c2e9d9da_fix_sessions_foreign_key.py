"""fix sessions foreign key

Revision ID: 43b0c2e9d9da
Revises: 835e658761a1
Create Date: 2026-06-23 02:06:13.134802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43b0c2e9d9da'
down_revision: Union[str, Sequence[str], None] = '835e658761a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
