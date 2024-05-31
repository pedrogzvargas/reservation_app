from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql


from app.config.database import Base


class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(postgresql.UUID(as_uuid=True), primary_key=True)
    passenger_id = Column(
        postgresql.UUID(as_uuid=True),
        ForeignKey("passengers.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    seat = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())
