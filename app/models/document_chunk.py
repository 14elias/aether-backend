from sqlalchemy import ForeignKey, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(primary_key=True)

    file_id: Mapped[int] = mapped_column(
        ForeignKey("files.id", ondelete="CASCADE"), index=True
    )

    workspace_id: Mapped[int] = mapped_column(
        ForeignKey("workspaces.id", ondelete="CASCADE"), index=True
    )

    content: Mapped[str] = mapped_column(Text)

    # MySQL does not support native vector like Postgres + pgvector
    # So we store embedding as JSON array of floats
    embedding: Mapped[list] = mapped_column(JSON)

    file = relationship("File", back_populates="chunks")
