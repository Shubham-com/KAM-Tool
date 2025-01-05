# app/api/performances.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, db
from typing import List

router = APIRouter()

@router.post("/performances/", response_model=schemas.Performance)
def create_performance(performance: schemas.PerformanceCreate, db: Session = Depends(db.get_db)):
    return crud.create_performance(db=db, performance=performance)

# Read all performance records
@router.get("/performances/", response_model=List[schemas.Performance])
def read_performances(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    return crud.get_performances(db=db, skip=skip, limit=limit)

# Read a single performance record by ID
@router.get("/performances/{performance_id}", response_model=schemas.Performance)
def read_performance(performance_id: int, db: Session = Depends(db.get_db)):
    performance = crud.get_performance(db=db, performance_id=performance_id)
    if not performance:
        raise HTTPException(status_code=404, detail="Performance not found")
    return performance

# Update a performance record
@router.put("/performances/{performance_id}", response_model=schemas.Performance)
def update_performance(performance_id: int, performance: schemas.PerformanceUpdate, db: Session = Depends(db.get_db)):
    updated_performance = crud.update_performance(db=db, performance_id=performance_id, performance=performance)
    if not updated_performance:
        raise HTTPException(status_code=404, detail="Performance not found")
    return updated_performance

# Delete a performance record
@router.delete("/performances/{performance_id}")
def delete_performance(performance_id: int, db: Session = Depends(db.get_db)):
    success = crud.delete_performance(db=db, performance_id=performance_id)
    if not success:
        raise HTTPException(status_code=404, detail="Performance not found")
    return {"detail": "Performance deleted successfully"}

