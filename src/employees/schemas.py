from pydantic import BaseModel


class EmployeeBase(BaseModel):
    id: int
    name: str
    position: str


class EmployeeCreate(EmployeeBase):
    class Config:
        orm_mode = True


class EmployeeUpdate(EmployeeCreate):
    pass
