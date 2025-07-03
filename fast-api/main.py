from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/')
async def root():
    return FileResponse('fast-api/index.html')

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post('/calculate')
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {'result' : result}
