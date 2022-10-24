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
