from sqlalchemy.orm import Session

from src.models.tasks_model import Task
from src.schemas.tasks_schemas import TaskCreate, TaskUpdate


def create_task(db: Session, task: TaskCreate):
    # new_task = Task(**task.model_dump())
    new_task = Task(
        name=task.name,
        is_parent_task=task.is_parent_task,
        deadline=task.deadline,
        status=task.status,
        executor_id=task.executor_id,
        parent_task_id=task.parent_task_id,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task: Task, task_update: TaskUpdate):
    for name, value in task_update.model_dump().items():
        setattr(task, name, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db=db, task_id=task_id)
    db.delete(task)
    db.commit()
