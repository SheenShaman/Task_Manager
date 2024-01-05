from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import String, Integer, Column, Boolean, ForeignKey, TIMESTAMP


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_parent_task = Column(Boolean, default=False)
    deadline = Column(TIMESTAMP)  # прописать дефолт (now + 30 days)
    status = Column(String)  # сделать список из вариантов статусов?

    parent_task_id = Column(Integer, ForeignKey("task.id"), nullable=True)
    exicuter_id = Column(Integer, ForeignKey("employee.id"))
    parent_task = relationship("Task", remote_side="Task.id", backref="subtasks")
    exicuter = relationship("Employee", back_populates="tasks")
