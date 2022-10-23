from fastapi import FastAPI
import uvicorn, colorama, multiprocessing

colorama.init()

app_api = FastAPI()
@app_api.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
  multiprocessing.freeze_support()
  uvicorn.run('main:app_api', host='127.0.0.1', port=4557, reload=False, workers=1)