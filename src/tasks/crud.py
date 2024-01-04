from sqlalchemy.orm import Session

from tasks.models import Task
from tasks.schemas import TaskCreate


def create_task(db: Session, task: TaskCreate):
    new_task = Task(**task.model_dump())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task: TaskCreate):
    for name, value in task.model_dump(exclude_unset=False).items():
        setattr(task, name, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db=db, task_id=task_id)
    db.delete(task)
    db.commit()
