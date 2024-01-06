from fastapi import FastAPI
from routers.tasks_router import router as task_router
from routers.employees_router import router as employee_router

app = FastAPI()

app.include_router(task_router)
app.include_router(employee_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)