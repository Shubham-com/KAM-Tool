# app/api/interactions.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, db
from typing import List

router = APIRouter()

@router.post("/interactions/", response_model=schemas.Interaction)
def create_interaction(interaction: schemas.InteractionCreate, db: Session = Depends(db.get_db)):
    return crud.create_interaction(db=db, interaction=interaction)

@router.get("/interactions/", response_model=List[schemas.Interaction])
def read_interactions(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    return crud.get_interactions(db=db, skip=skip, limit=limit)

@router.get("/interactions/{interaction_id}", response_model=schemas.Interaction)
def read_interaction(interaction_id: int, db: Session = Depends(db.get_db)):
    interaction = crud.get_interaction(db=db, interaction_id=interaction_id)
    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return interaction

@router.put("/interactions/{interaction_id}", response_model=schemas.Interaction)
def update_interaction(interaction_id: int, interaction: schemas.InteractionUpdate, db: Session = Depends(db.get_db)):
    updated_interaction = crud.update_interaction(db=db, interaction_id=interaction_id, interaction=interaction)
    if not updated_interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return updated_interaction

@router.delete("/interactions/{interaction_id}")
def delete_interaction(interaction_id: int, db: Session = Depends(db.get_db)):
    success = crud.delete_interaction(db=db, interaction_id=interaction_id)
    if not success:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return {"detail": "Interaction deleted successfully"}
