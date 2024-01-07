from typing import List, Type, Union
from sqlalchemy.orm import Session

from models import Task
from schemas.tasks_schemas import TaskCreate, TaskUpdate


class TaskCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task_schema: TaskCreate) -> Task:
        """ Create Task """
        new_task = Task(**task_schema.model_dump(exclude_unset=True))
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)
        return new_task

    def get_tasks(self, skip: int = 0, limit: int = 100) -> List[Type[Task]]:
        """ Get Tasks """
        return self.db.query(Task).offset(skip).limit(limit).all()

    def get_task_by_id(self, task_id: int) -> Union[Task, None]:
        """ Get Task by id """
        return self.db.query(Task).filter_by(id=task_id).first()

    def update_task(self, task_id: int, task_schema: TaskUpdate) -> Union[Task, None]:
        """ Update Task """
        updated_task = self.get_task_by_id(task_id=task_id)
        if updated_task:
            for field, value in task_schema.model_dump(exclude_unset=True).items():
                setattr(updated_task, field, value)
            self.db.commit()
            self.db.refresh(updated_task)
        return updated_task

    def delete_task(self, task_id: int) -> Union[Task, None]:
        """ Delete Task """
        task = self.get_task_by_id(task_id=task_id)
        if task:
            self.db.delete(task)
            self.db.commit()
        return task
