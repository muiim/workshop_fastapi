from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/todos")
async def get_todos():
    return [
        {"id": 1,"detail": "first "},
        {"id": 2,"detail": "second"}
    ]

counter = 0
@app.get("/counter")
async def get_counter():
    global counter
    counter += 1
    return {"message": f"counter = {counter}"}
