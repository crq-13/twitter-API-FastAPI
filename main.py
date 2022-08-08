

# FastAPI
from fastapi import FastAPI

# Models
import models

app = FastAPI()




@app.get(path=("/"))
def home():
    return {"Twitter API": "Working"}

