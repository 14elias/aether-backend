from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class WorkspaceMember(Base):
    __tablename__ = "workspace_members"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), index=True
    )

    workspace_id: Mapped[int] = mapped_column(
        ForeignKey("workspaces.id", ondelete="CASCADE"), index=True
    )

    role: Mapped[str] = mapped_column(
        String(50)
    )  # ADMIN | CONTRIBUTOR | VIEWER

    user = relationship("User", back_populates="workspace_memberships")
    workspace = relationship("Workspace", back_populates="members")
