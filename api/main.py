from typing import Optional
try:
  from schemas import Symlink, Status, SymlinkByHash
except:
  from .schemas import Symlink, Status, SymlinkByHash
from fastapi import FastAPI
import uvicorn, colorama, multiprocessing

colorama.init()
app_api = FastAPI()

@app_api.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-models-path-by-name")
def get_models_path_by_name(name1: str, name2: str, name3: Optional[str] = None): # url: /get-models-path-by-name?name1=...&name2=...&name3=... where name3 is optional
    return {"path": "/this/test/path"}

@app.get("/download_models_by_name")
def download_models_by_name(name1: str, name2: str, name3: str): # url: /download_models_by_name?name1=...&name2=...&name3=...
    return {"path": "/this/test/path", "download": "complete"}

@app.get("/get_model_details_by_name")
def get_model_details_by_name(name1: str, name2: str, name3: str): # url: /get_model_details_by_name?name1=...&name2=...&name3=...
    return {"info": "json array"}

@app.get("/get_models_path_by_hash")
def get_models_path_by_hash(hash1: str, hash2: str, hash3: str): # url: /get_models_path_by_hash?hash1=...&hash2=...&hash3=...
    return {"path": "/this/test/path"}

@app.get("/download_models_by_hash")
def download_models_by_hash(hash1: str, hash2: str, hash3: str): # url: /download_models_by_hash?hash1=...&hash2=...&hash3=...
    return {"path": "/this/test/path", "download": "complete"}

@app.get("/get_model_details_by_hash")
def get_model_details_by_hash(hash1: str, hash2: str, hash3: str): # url: /get_model_details_by_hash?hash1=...&hash2=...&hash3=...
    return {"info": "json array"}

@app.post("/symlink_by_name", response_model=Status)
def symlink_by_name(data: Symlink): # url: /symlink_by_name
    return {"status": "success"}

@app.post("/symlink_by_hash", response_model=Status)
def symlink_by_hash(data: SymlinkByHash): # url: /symlink_by_hash?hash=...&symlink_location=...
    return {"status": "success"}

if __name__ == "__main__":
  multiprocessing.freeze_support()
  uvicorn.run('main:app_api', host='127.0.0.1', port=4557, reload=False, workers=1)