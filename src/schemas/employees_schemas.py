from pydantic import BaseModel
from typing import Optional, List
from src.schemas.tasks_schemas import TaskRead


class EmployeeRead(BaseModel):
    id: int
    name: str
    position: str
    is_busy: Optional[bool] = False
    tasks: Optional[List[TaskRead]] = None

    class Config:
        from_attributes = True


class EmployeeCreate(BaseModel):
    name: str
    position: str
    is_busy: Optional[bool] = False
    tasks: Optional[list[str]] = None


class EmployeeUpdate(BaseModel):
    name: str
    position: Optional[str] = None
    is_busy: Optional[bool] = False
