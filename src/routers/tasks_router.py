from typing import List, Type
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from crud.tasks_crud import TaskCRUD
from schemas.tasks_schemas import TaskRead, TaskCreate, TaskUpdate, ImportantTask

router = APIRouter(
    prefix="/tasks",
    tags=["Task"],
)


@router.post("/create/", response_model=TaskRead)
def create_task(task_schema: TaskCreate, db: Session = Depends(get_db)) -> TaskRead:
    """ Create Task """
    try:
        task_crud = TaskCRUD(db=db)
        created_task = task_crud.create_task(task_schema=task_schema)
        return created_task
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=List[TaskRead])
def get_tasks(db: Session = Depends(get_db)) -> List[Type[TaskRead]]:
    """ Get Tasks """
    try:
        task_crud = TaskCRUD(db=db)
        tasks = task_crud.get_tasks()
        if tasks is None:
            raise HTTPException(status_code=404, detail="Tasks not found")
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)) -> TaskRead:
    """ Get Task """
    try:
        task_crud = TaskCRUD(db=db)
        task = task_crud.get_task_by_id(task_id=task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/important_tasks/', response_model=List[ImportantTask])
def get_important_tasks(db: Session = Depends(get_db)) -> List[ImportantTask]:
    """  """
    try:
        task_crud = TaskCRUD(db=db)
        important_tasks = task_crud.get_important_tasks()
        if not important_tasks:
            raise HTTPException(status_code=404, detail='Important tasks not founded')
        return important_tasks
    except HTTPException as e:
        print(f"Exception details: {e.detail}")
        raise e
    except Exception as e:
        print(f"Unexpected exception: {str(e)}")
        raise HTTPException(status_code=500, detail='Internal Server Error')


@router.patch("/update/{task_id}")
def update_task(task_schema: TaskUpdate, task_id: int, db: Session = Depends(get_db)) -> TaskRead:
    """ Update Task """
    try:
        task_crud = TaskCRUD(db=db)
        updated_task = task_crud.update_task(task_id=task_id, task_schema=task_schema)
        return updated_task
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """ Delete Task """
    try:
        task_crud = TaskCRUD(db=db)
        deleted_task = task_crud.delete_task(task_id=task_id)
        return deleted_task
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
