from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return "Hello, World!"


@app.on_event("startup")
def start():
    import database
    from models import Employee

    database.Base.metadata.create_all(database.engine)
