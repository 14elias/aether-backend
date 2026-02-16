from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.models.base import Base


class File(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True)

    filename: Mapped[str] = mapped_column(String(255))
    storage_path: Mapped[str] = mapped_column(String(500))
    size: Mapped[int] = mapped_column(Integer)

    workspace_id: Mapped[int] = mapped_column(
        ForeignKey("workspaces.id", ondelete="CASCADE"), index=True
    )

    uploaded_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"), index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    workspace = relationship("Workspace", back_populates="files")
    uploaded_by_user = relationship("User", back_populates="uploaded_files")
    chunks = relationship(
        "DocumentChunk", back_populates="file", cascade="all, delete-orphan"
    )
