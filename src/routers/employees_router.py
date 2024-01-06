from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.crud.employees_crud import EmployeeCRUD
from src.schemas.employees_schemas import EmployeeRead, EmployeeCreate, EmployeeUpdate
from src.db.database import get_db

router = APIRouter(
    prefix="/employees",
    tags=["Employee"],
)


@router.post("/create/", response_model=EmployeeRead)
async def create_employee(employee_schema: EmployeeCreate, db: Session = Depends(get_db)):
    """ Create Employee"""
    employee_crud = EmployeeCRUD(db=db)
    created_employee = employee_crud.create_employee(employee_schema=employee_schema)
    return created_employee


@router.get("/", response_model=EmployeeRead)
async def get_employees(db: Session = Depends(get_db)):
    """ Get Employees"""
    employee_crud = EmployeeCRUD(db=db)
    employees = employee_crud.get_employees()
    return employees


@router.get("/{employee_id}", response_model=EmployeeRead)
async def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """ Get Employee by id"""
    employee_crud = EmployeeCRUD(db=db)
    employee = employee_crud.get_employee_by_id(employee_id=employee_id)
    return employee


@router.patch("/update/{employee_id}", response_model=EmployeeRead)
async def update_employee(employee_schema: EmployeeUpdate, employee_id: int, db: Session = Depends(get_db)):
    """ Update Employee"""
    employee_crud = EmployeeCRUD(db=db)
    updated_employee = employee_crud.update_employee(employee_id=employee_id, employee_schema=employee_schema)
    return updated_employee


@router.delete("/delete/{employee_id}")
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """ Delete Employee"""
    employee_crud = EmployeeCRUD(db=db)
    deleted_employee = employee_crud.delete_employee(employee_id=employee_id)
    return deleted_employee
