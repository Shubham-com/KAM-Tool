# app/api/employees.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, db
from typing import List

router = APIRouter()

# Endpoint to create an employee
@router.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(db.get_db)):
    return crud.create_employee(db=db, employee=employee)

# Read all employees
@router.get("/employees/", response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    return crud.get_employees(db=db, skip=skip, limit=limit)

# Read a single employee by ID
@router.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(db.get_db)):
    employee = crud.get_employee(db=db, employee_id=employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# Update an employee
@router.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(db.get_db)):
    updated_employee = crud.update_employee(db=db, employee_id=employee_id, employee=employee)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

# Delete an employee
@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(db.get_db)):
    success = crud.delete_employee(db=db, employee_id=employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted successfully"}


