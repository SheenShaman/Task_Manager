from sqlalchemy.orm import Session

from employees.models import Employee
from employees.employees_schemas import EmployeeCreate, EmployeeUpdate


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


def update_employee(db: Session, employee: Employee, employee_update: EmployeeUpdate):
    for name, value in employee_update.model_dump().items():
        setattr(employee, name, value)
    db.commit()
    db.refresh(employee)
    return employee


def delete_employee(db: Session, employee_id: int):
    employee = get_employee_by_id(db=db, employee_id=employee_id)
    db.delete(employee)
    db.commit()
