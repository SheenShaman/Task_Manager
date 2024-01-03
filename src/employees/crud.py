from sqlalchemy.orm import Session
from models import Employee
from schemas import EmployeeSchema


def create_employee(db: Session, employee: EmployeeSchema):
    db_item = Employee(name=employee.name, position=employee.position)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employee).offset(skip).limit(limit).all()


def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def update_employee(db: Session, employee_id: int, name: str, position: str):
    db_item = get_employee_by_id(db=db, employee_id=employee_id)

    db_item.name = name
    db_item.position = position

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_employee(db: Session, employee_id: int):
    db_item = get_employee_by_id(db=db, employee_id=employee_id)
    db.delete(db_item)
    db.commit()
