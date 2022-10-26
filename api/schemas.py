from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Symlink(BaseModel):
    name: str
    symlink: str
    location: str

class Status(BaseModel):
    status: str = "success"
    info: Optional[str] = None

class SymlinkByHash(BaseModel):
    hash: str
    symlink_location: str

class ProjectIn(BaseModel):
    name: str
    description: str
    md5: str

    class Config:
        orm_mode = True

class ProjectOut(BaseModel):
    id: str
    name: str
    description: str
    md5: str
    created_at: datetime

    class Config:
        orm_mode = True
