from datetime import datetime

from pydantic import BaseModel


class TaskBase(BaseModel):
    id: int
    name: str
    is_parent_task: bool
    deadline: datetime
    status: str


class TaskCreate(TaskBase):
    class Config:
        orm_mode = True
