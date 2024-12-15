# app/schemas.py

from pydantic import BaseModel

class TermBase(BaseModel):
    keyword: str
    description: str

class TermCreate(TermBase):
    pass

class Term(TermBase):
    id: int

    class Config:
        orm_mode = True
