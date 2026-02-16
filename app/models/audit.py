from sqlalchemy import String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.models.base import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), index=True
    )

    workspace_id: Mapped[int] = mapped_column(
        ForeignKey("workspaces.id"), index=True
    )

    action: Mapped[str] = mapped_column(String(100))
    metadata: Mapped[dict] = mapped_column(JSON)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
