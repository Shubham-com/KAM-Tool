# app/api/lead_contacts.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, db
from typing import List

router = APIRouter()

@router.post("/lead_contacts/", response_model=schemas.LeadContact)
def create_lead_contact(contact: schemas.LeadContactCreate, db: Session = Depends(db.get_db)):
    return crud.create_lead_contact(db=db, contact=contact)

@router.get("/lead-contacts/", response_model=List[schemas.LeadContact])
def read_lead_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    return crud.get_lead_contacts(db=db, skip=skip, limit=limit)

@router.get("/lead-contacts/{contact_id}", response_model=schemas.LeadContact)
def read_lead_contact(contact_id: int, db: Session = Depends(db.get_db)):
    contact = crud.get_lead_contact(db=db, contact_id=contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="LeadContact not found")
    return contact

@router.put("/lead-contacts/{contact_id}", response_model=schemas.LeadContact)
def update_lead_contact(contact_id: int, contact: schemas.LeadContactUpdate, db: Session = Depends(db.get_db)):
    updated_contact = crud.update_lead_contact(db=db, contact_id=contact_id, contact=contact)
    if not updated_contact:
        raise HTTPException(status_code=404, detail="LeadContact not found")
    return updated_contact

@router.delete("/lead-contacts/{contact_id}")
def delete_lead_contact(contact_id: int, db: Session = Depends(db.get_db)):
    success = crud.delete_lead_contact(db=db, contact_id=contact_id)
    if not success:
        raise HTTPException(status_code=404, detail="LeadContact not found")
    return {"detail": "LeadContact deleted successfully"}
