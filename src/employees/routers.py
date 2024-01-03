from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from employees import crud
from schemas import EmployeeSchema
from utils.utils import get_db

router = APIRouter(
    prefix="/employees",
    tags=["Employee"],
)


@router.post("/create/")
async def create_employee(employee: EmployeeSchema, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


@router.get("/")
async def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_employees(db=db, skip=skip, limit=limit)


@router.get("/{employee_id}")
async def get_employee(employee_id: int, db: Session = Depends(get_db)):
    return crud.get_employee_by_id(db=db, employee_id=employee_id)


@router.patch("/update/{employee_id}")
async def update_employee(employee_id: int, name: str, position: str, db: Session = Depends(get_db)):
    return crud.update_employee(db=db, employee_id=employee_id, name=name, position=position)


@router.delete("/delete/{employee_id}")
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    return crud.delete_employee(db=db, employee_id=employee_id)
