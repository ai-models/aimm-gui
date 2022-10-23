import uvicorn
from fastapi import FastAPI

app_api = FastAPI()
@app_api.get("/")
async def root():
    return {"message": "Hello World"}

uvicorn.run("api.api:app_api", host='127.0.0.1', port=4557, reload=True, workers=3)
