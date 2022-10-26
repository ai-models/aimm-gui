try:
  from schemas import Symlink, Status, SymlinkByHash
except:
  from .schemas import Symlink, Status, SymlinkByHash
from fastapi import FastAPI
import uvicorn, colorama, multiprocessing

colorama.init()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_path")
def get_models_path_by_name(project_name, by='name'):

    return {"path": "/this/test/path"}

@app.get("/install")
def download_models_by_name(project_name, by='name'):
    return {"path": "/this/test/path", "download": "complete"}

@app.get("/get_details")
def get_model_details_by_name(project_name, by='name'):
    return {"info": "json array"}

@app.post("/symlink", response_model=Status)
def symlink_by_name(project_name, by='name', destination='path'):
    return {"status": "success"}

if __name__ == "__main__":
  multiprocessing.freeze_support()
  uvicorn.run('main:app', host='127.0.0.1', port=4557, reload=False, workers=1)