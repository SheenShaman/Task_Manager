from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import String, Integer, Column


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    position = Column(String)

    tasks = relationship("Task")
