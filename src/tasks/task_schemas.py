from datetime import datetime

from pydantic import BaseModel


class TaskBase(BaseModel):
    id: int
    name: str
    is_parent_task: bool
    deadline: datetime
    status: str
    exicuter_id: int

    class Config:
        from_attributes = True


class TaskCreate(TaskBase):
    name: str
    is_parent_task: bool
    deadline: datetime
    status: str
    parent_task_id: int
    exicuter_id: int

    # class Config:
    #     orm_mode = True


class TaskUpdate(BaseModel):
    parent_task_id: int
    name: str
    deadline: datetime
    status: str
    exicuter_id: int
