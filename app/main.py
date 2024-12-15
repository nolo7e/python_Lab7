# app/main.py

from fastapi import FastAPI, HTTPException, Depends
from typing import List, Optional
import models
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy import or_

# Создаем все таблицы
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Глоссарий API")

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/terms/", response_model=List[schemas.Term])
def read_terms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    terms = db.query(models.Term).offset(skip).limit(limit).all()
    return terms

@app.get("/terms/search/", response_model=List[schemas.Term])
def search_terms(keyword: str, db: Session = Depends(get_db)):
    terms = db.query(models.Term).filter(models.Term.keyword.ilike(f"%{keyword}%")).all()
    return terms

@app.get("/terms/{term_id}", response_model=schemas.Term)
def read_term(term_id: int, db: Session = Depends(get_db)):
    term = db.query(models.Term).filter(models.Term.id == term_id).first()
    if term is None:
        raise HTTPException(status_code=404, detail="Термин не найден")
    return term

@app.post("/terms/", response_model=schemas.Term)
def create_term(term: schemas.TermCreate, db: Session = Depends(get_db)):
    db_term = models.Term(**term.dict())
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term

@app.put("/terms/{term_id}", response_model=schemas.Term)
def update_term(term_id: int, term: schemas.TermCreate, db: Session = Depends(get_db)):
    db_term = db.query(models.Term).filter(models.Term.id == term_id).first()
    if db_term is None:
        raise HTTPException(status_code=404, detail="Термин не найден")
    for key, value in term.dict().items():
        setattr(db_term, key, value)
    db.commit()
    db.refresh(db_term)
    return db_term

@app.delete("/terms/{term_id}")
def delete_term(term_id: int, db: Session = Depends(get_db)):
    db_term = db.query(models.Term).filter(models.Term.id == term_id).first()
    if db_term is None:
        raise HTTPException(status_code=404, detail="Термин не найден")
    db.delete(db_term)
    db.commit()
    return {"detail": "Термин удален"}
