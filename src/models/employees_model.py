from sqlalchemy import String, Integer, Boolean, Column
from sqlalchemy.orm import relationship

from src.models import Base


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    is_busy = Column(Boolean, default=False)

    tasks = relationship('Task', back_populates='executor')
