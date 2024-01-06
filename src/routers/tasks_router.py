from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.crud import tasks_crud
from src.schemas.tasks_schemas import TaskCreate, TaskUpdate
from src.db.database import get_db

router = APIRouter(
    prefix="/tasks",
    tags=["Task"],
)


@router.post("/create/")
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return tasks_crud.create_task(db=db, task=task)


@router.get("/")
async def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return tasks_crud.get_tasks(db=db, skip=skip, limit=limit)


@router.get("/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_db)):
    return tasks_crud.get_task_by_id(db=db, task_id=task_id)


@router.patch("/update/{task_id}")
async def update_task(task_update: TaskUpdate, task_id: int, db: Session = Depends(get_db)):
    task = tasks_crud.get_task_by_id(db=db, task_id=task_id)
    return tasks_crud.update_task(db=db, task=task, task_update=task_update)


@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    return tasks_crud.delete_task(db=db, task_id=task_id)
