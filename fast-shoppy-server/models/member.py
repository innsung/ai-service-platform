from sqlalchemy import String, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base
from datetime import datetime, timezone

class MemberModel(Base):
    __tablename__ = "member"

    id: Mapped[str] = mapped_column(
        String(50), 
        primary_key=True
    )
    pwd: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )
    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=True
    )
    email: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )
    role: Mapped[str] = mapped_column(
        Enum("USER", "ADMIN", name="member_role"),
        nullable=False,
        default="USER"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )

