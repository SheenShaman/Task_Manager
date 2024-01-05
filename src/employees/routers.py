from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from employees import crud
from employees.employees_schemas import EmployeeCreate, EmployeeUpdate
from utils.utils import get_db

router = APIRouter(
    prefix="/employees",
    tags=["Employee"],
)


@router.post("/create/")
async def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


@router.get("/")
async def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_employees(db=db, skip=skip, limit=limit)


@router.get("/{employee_id}")
async def get_employee(employee_id: int, db: Session = Depends(get_db)):
    return crud.get_employee_by_id(db=db, employee_id=employee_id)


@router.patch("/update/{employee_id}")
async def update_employee(employee_update: EmployeeUpdate, employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee_by_id(db=db, employee_id=employee_id)
    return crud.update_employee(db=db, employee=employee, employee_update=employee_update)


@router.delete("/delete/{employee_id}")
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    return crud.delete_employee(db=db, employee_id=employee_id)


################################################################
@router.get("/{busy_employees}")
async def get_busy_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = crud.get_employees(db=db, skip=skip, limit=limit)
    x = []
    for emp in employees:
        x.append(emp)
    return x
