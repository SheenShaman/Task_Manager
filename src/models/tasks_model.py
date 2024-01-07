import datetime
from enum import Enum
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, Column, ForeignKey, DateTime, Enum as EnumType

from models import Base


class TaskStatus(str, Enum):
    NOT_STARTED = 'Not started'
    STARTED = 'Started'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    parent_task_id = Column(Integer, ForeignKey('task.id'), nullable=True)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    deadline = Column(DateTime, nullable=False, default=created_at + datetime.timedelta(days=30))

    status = Column(EnumType(TaskStatus, native_enum=False), default=TaskStatus.NOT_STARTED)
    executor_id = Column(Integer, ForeignKey("employee.id"))

    parent_task = relationship("Task", remote_side="Task.id", backref="subtasks")
    executor = relationship("Employee", back_populates="tasks")
