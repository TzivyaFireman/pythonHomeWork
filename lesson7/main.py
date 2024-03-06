import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from enum import Enum, IntEnum

app = FastAPI()

class statusEnum(str, Enum):
    open = 'open'
    close = 'close'

class Task(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    des:str
    id:int
    status: statusEnum


    @field_validator('des')
    def check_age(cls, des):
        if len(des) > 100:
            raise ValueError('error')
        return des


    @field_validator('id')
    def check_age(cls, id):
        if id > 10:
            raise ValueError('error')
        return id


tasks = {}

@app.get("/{id}")
async def get_task(id):
    return tasks


@app.post("/")
async def add_task(task: Task):
    try:
        tasks[task.id] = task
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {task.name}"


@app.put("/id", response_model=Task)
async def update_item(id: str, task: Task):
    update_tasks = jsonable_encoder(task)
    tasks[id] = update_tasks
    return update_tasks

@app.delete("/{id}")
async def delete_item(id: int):
    del tasks[id]
    return {"message": "Item deleted"}



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080)


