# app/api/leads.py
from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, db
from typing import List
from app import models
router = APIRouter()

@router.post("/leads/", response_model=schemas.Lead)
def create_lead(lead: schemas.LeadCreate, db: Session = Depends(db.get_db)):
    return crud.create_lead(db=db, lead=lead)

@router.get("/leads/", response_model=List[schemas.Lead])
def read_leads(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    return crud.get_leads(db=db, skip=skip, limit=limit)

@router.get("/leads/{lead_id}", response_model=schemas.Lead)
def read_lead(lead_id: int, db: Session = Depends(db.get_db)):
    lead = crud.get_lead(db=db, lead_id=lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

@router.put("/leads/{lead_id}", response_model=schemas.Lead)
def update_lead(lead_id: int, lead: schemas.LeadUpdate, db: Session = Depends(db.get_db)):
    updated_lead = crud.update_lead(db=db, lead_id=lead_id, lead=lead)
    if not updated_lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return updated_lead

@router.delete("/leads/{lead_id}")
def delete_lead(lead_id: int, db: Session = Depends(db.get_db)):
    success = crud.delete_lead(db=db, lead_id=lead_id)
    if not success:
        raise HTTPException(status_code=404, detail="Lead not found")
    return {"detail": "Lead deleted successfully"}
