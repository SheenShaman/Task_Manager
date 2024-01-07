from typing import List, Type
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from crud.employees_crud import EmployeeCRUD
from schemas.employees_schemas import EmployeeRead, EmployeeCreate, EmployeeUpdate

router = APIRouter(
    prefix="/employees",
    tags=["Employee"],
)


@router.post("/create/", response_model=EmployeeRead)
def create_employee(employee_schema: EmployeeCreate, db: Session = Depends(get_db)) -> EmployeeRead:
    """ Create Employee """
    try:
        employee_crud = EmployeeCRUD(db=db)
        created_employee = employee_crud.create_employee(employee_schema=employee_schema)
        return created_employee
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=List[EmployeeRead])
def get_employees(db: Session = Depends(get_db)) -> List[Type[EmployeeRead]]:
    """ Get Employees """
    try:
        employee_crud = EmployeeCRUD(db=db)
        employees = employee_crud.get_employees()
        if employees is None:
            raise HTTPException(status_code=404, detail='Employees not found')
        return employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{employee_id}", response_model=EmployeeRead)
def get_employee(employee_id: int, db: Session = Depends(get_db)) -> EmployeeRead:
    """ Get Employee by id """
    try:
        employee_crud = EmployeeCRUD(db=db)
        employee = employee_crud.get_employee_by_id(employee_id=employee_id)
        if employee is None:
            raise HTTPException(status_code=404, detail='Employee not found')
        return employee
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/busy_employees", response_model=List[EmployeeRead])
def get_busy_employees(db: Session = Depends(get_db)) -> List[EmployeeRead]:
    """ Get Busy Employees """
    try:
        employee_crud = EmployeeCRUD(db=db)
        busy_employees = employee_crud.get_busy_employees()
        if not busy_employees:
            raise HTTPException(status_code=404, detail='Busy employees not found')
        return busy_employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/update/{employee_id}", response_model=EmployeeRead)
def update_employee(employee_schema: EmployeeUpdate, employee_id: int, db: Session = Depends(get_db)) -> EmployeeRead:
    """ Update Employee """
    try:
        employee_crud = EmployeeCRUD(db=db)
        updated_employee = employee_crud.update_employee(employee_id=employee_id, employee_schema=employee_schema)
        return updated_employee
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)) -> EmployeeRead:
    """ Delete Employee """
    try:
        employee_crud = EmployeeCRUD(db=db)
        deleted_employee = employee_crud.delete_employee(employee_id=employee_id)
        return deleted_employee
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
