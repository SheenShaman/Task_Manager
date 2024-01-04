from fastapi import FastAPI
from tasks.routers import router as task_router
from employees.routers import router as employee_router

app = FastAPI()
app.include_router(task_router)
app.include_router(employee_router)


@app.get("/")
def hello():
    return "Hello, World!"


@app.on_event("startup")
def start():
    import database
    from tasks.models import Task
    from employees.models import Employee

    database.Base.metadata.create_all(database.engine)
