from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tasks import crud
from tasks.schemas import TaskCreate, TaskUpdate
from utils.utils import get_db

router = APIRouter(
    prefix="/tasks",
    tags=["Task"],
)


@router.post("/create/")
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)


@router.get("/")
async def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tasks(db=db, skip=skip, limit=limit)


@router.get("/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_db)):
    return crud.get_task_by_id(db=db, task_id=task_id)


@router.patch("/update/{task_id}")
async def update_task(task_update: TaskUpdate, task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db=db, task_id=task_id)
    return crud.update_task(db=db, task=task, task_update=task_update)


@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db=db, task_id=task_id)
