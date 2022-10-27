from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional, Union
import uvicorn, colorama, multiprocessing

try:
  from schemas import Status, ProjectIn, ProjectOut
  from database import Base, engine, get_db
  from models import Project
except:
  from .database import Base, engine, get_db
  from .schemas import Status, ProjectIn, ProjectOut
  from .models import Project

colorama.init()
app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.post("/import-from-json", response_model=List[ProjectOut], status_code=status.HTTP_201_CREATED)
def import_from_json(projects_json: List[ProjectIn], db: Session = Depends(get_db)):  # url: /import-from-json
  """
  Import projects from JSON file to database.
  """
  projects = []
  for project in projects_json:
    project_to_create = Project(**project.dict())
    db.add(project_to_create)
    db.commit()
    db.refresh(project_to_create)
    projects.append(project_to_create)
  return projects


@app.get("/projects", response_model=List[ProjectOut])
def get_projects(search: Union[List[str], None] = Query(default=None), by: Optional[str] = 'name',
                 db: Session = Depends(get_db)):  # url: /projects?search=project1&search=project2&by=name
  """
  Get all projects from database. Optionally, filter by names. i.e. /projects?search=project1&search=project2
  """
  try:
    if search:
      projects = db.query(Project).filter(getattr(Project, by).in_(search)).all()
    else:
      projects = db.query(Project).all()
    if not projects:
      raise AttributeError
  except AttributeError:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with {by} in {search} not found.")
  return projects


@app.get("/projects/{id}", response_model=ProjectOut, status_code=status.HTTP_200_OK)
def get_project(id: int, db: Session = Depends(get_db)):  # url: /projects/1
  """
  Get project by id.
  """
  project = db.query(Project).filter(Project.id == id).first()
  if not project:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with id {id} not found.")
  return project


@app.post("/projects", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectIn, db: Session = Depends(get_db)):  # url: /projects
  """
  Create a new project.
  """
  project_to_create = Project(**project.dict())
  db.add(project_to_create)
  db.commit()
  db.refresh(project_to_create)
  return project_to_create


@app.put("/projects/{id}", response_model=ProjectOut, status_code=status.HTTP_202_ACCEPTED)
def update_project(id: int, project: ProjectIn, db: Session = Depends(get_db)):  # url: /projects/1
  """
  Update a project by id.
  """
  project_to_update = db.query(Project).filter(Project.id == id).first()
  if not project_to_update:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with id {id} not found.")
  project_to_update.name = project.name
  project_to_update.description = project.description
  project_to_update.md5 = project.md5
  db.commit()
  db.refresh(project_to_update)
  return project_to_update


@app.delete("/projects/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(id: int, db: Session = Depends(get_db)):  # url: /projects/1
  """
  Delete a project by id.
  """
  project_to_delete = db.query(Project).filter(Project.id == id).first()
  if not project_to_delete:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with id {id} not found.")
  db.delete(project_to_delete)
  db.commit()


@app.get("/get_project_details", response_model=ProjectOut, status_code=status.HTTP_200_OK)
def get_model_details(search: str, by: Optional[str] = 'name', db: Session = Depends(
  get_db)):  # url: /project_get_details?search=project1&search=project2&by=name
  """
  Get single project from database. Optionally, filter by names. i.e. /projects?search=project1&search=project2
  """
  try:
    project = db.query(Project).filter(getattr(Project, by) == search).first()
    if not project:
      raise AttributeError
  except AttributeError:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with {by} = {search} not found.")
  return project


@app.get("/get_projects_details", response_model=List[ProjectOut], status_code=status.HTTP_200_OK)
def get_multiple_projects_details(search: List[str] = Query(default=[]), by: Optional[str] = 'name',
                                  db: Session = Depends(
                                    get_db)):  # url: /projects_get_details?search=project1&search=project2&by=name
  """
  Get all projects from database. Optionally, filter by names. i.e. /projects?search=project1&search=project2
  DUPLICATE OF get_projects
  """
  try:
    projects = db.query(Project).filter(getattr(Project, by).in_(search)).all()
    if not projects:
      raise AttributeError
  except AttributeError:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Project with {by} {search} not found.")
  return projects


@app.get("/get_path")
def get_models_path(project_name, by='name'):
  return {"path": "/this/test/path"}


@app.get("/install")
def download_models(project_name, by='name'):
  return {"path": "/this/test/path", "download": "complete"}


@app.post("/symlink", response_model=Status)
def symlink(project_name, by='name', destination='path'):
  return {"status": "success"}


if __name__ == "__main__":
  multiprocessing.freeze_support()
  uvicorn.run('main:app', host='127.0.0.1', port=4557, reload=False, workers=1)
