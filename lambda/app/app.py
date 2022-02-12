from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "pong1"}

handler = Mangum(app)
