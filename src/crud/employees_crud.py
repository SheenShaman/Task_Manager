from typing import List, Type, Union
from sqlalchemy.orm import Session

from models import Employee
from schemas.employees_schemas import EmployeeCreate, EmployeeUpdate


class EmployeeCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, employee_schema: EmployeeCreate) -> Employee:
        """ Create Employee """
        # is_busy_value = employee_schema.is_busy if employee_schema.is_busy is not None else False
        #
        # new_employee = Employee(name=employee_schema.name,
        #                         position=employee_schema.position,
        #                         is_busy=is_busy_value)
        new_employee = Employee(**employee_schema.model_dump(exclude_unset=True))
        self.db.add(new_employee)
        self.db.commit()
        self.db.refresh(new_employee)
        return new_employee

    def get_employees(self, skip: int = 0, limit: int = 100) -> List[Type[Employee]]:
        """ Get Employees """
        return self.db.query(Employee).offset(skip).limit(limit).all()

    def get_employee_by_id(self, employee_id: int) -> Union[Employee, None]:
        """ Get Employee by id """
        return self.db.query(Employee).filter_by(id=employee_id).first()

    def update_employee(self, employee_id: int, employee_schema: EmployeeUpdate) -> Union[Employee, None]:
        """ Update Employee """
        updated_employee = self.get_employee_by_id(employee_id=employee_id)
        if updated_employee:
            for field, value in employee_schema.model_dump(exclude_unset=True).items():
                setattr(updated_employee, field, value)
            self.db.commit()
            self.db.refresh(updated_employee)
        return updated_employee

    def delete_employee(self, employee_id: int) -> Union[Employee, None]:
        """ Delete Employee """
        employee = self.get_employee_by_id(employee_id=employee_id)
        if employee:
            self.db.delete(employee)
            self.db.commit()
        return employee
