from sqlalchemy.orm import Session

from employees.models import Employee
from employees.schemas import EmployeeCreate


def create_employee(db: Session, employee: EmployeeCreate):
    new_employee = Employee(**employee.model_dump())

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employee).offset(skip).limit(limit).all()


def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def update_employee(db: Session, employee_id: int, name: str, position: str):
    new_employee = get_employee_by_id(db=db, employee_id=employee_id)

    new_employee.name = name
    new_employee.position = position

    db.commit()
    db.refresh(new_employee)
    return new_employee


def delete_employee(db: Session, employee_id: int):
    employee = get_employee_by_id(db=db, employee_id=employee_id)
    db.delete(employee)
    db.commit()
