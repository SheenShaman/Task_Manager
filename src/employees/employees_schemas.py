from pydantic import BaseModel
from typing import Optional, List
from tasks.task_schemas import TaskBase


class EmployeeBase(BaseModel):
    id: int
    name: str
    position: str
    tasks: Optional[List[TaskBase]] = None


class EmployeeCreate(EmployeeBase):
    name: str
    position: str
    tasks: Optional[List[TaskBase]] = None

    class Config:
        orm_mode = True


class EmployeeUpdate(EmployeeCreate):
    name: str
    position: str
