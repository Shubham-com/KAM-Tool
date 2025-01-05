# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas
from app.schemas import InteractionUpdate  # Import InteractionUpdate
from fastapi import HTTPException

# CRUD operations for Leads
def create_lead(db: Session, lead: schemas.LeadCreate):
    db_lead = models.Lead(name=lead.name, status=lead.status, is_active=lead.is_active)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

def get_leads(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Lead).offset(skip).limit(limit).all()

# Function to retrieve a lead by its ID
def get_lead(db: Session, lead_id: int):
    return db.query(models.Lead).filter(models.Lead.id == lead_id).first()

def update_lead(db: Session, lead_id: int, lead: schemas.LeadUpdate):
    db_lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()
    if db_lead:
        db_lead.name = lead.name
        db_lead.status = lead.status
        db_lead.is_active = lead.is_active
        db.commit()
        db.refresh(db_lead)
        return db_lead
    return None

def delete_lead(db: Session, lead_id: int):
    # Query for the lead to delete
    db_lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()
    
    if db_lead:
        db.delete(db_lead)
        db.commit()  # Commit the transaction to delete the lead
        return True
    return False

# CRUD operations for LeadContacts
def create_lead_contact(db: Session, contact: schemas.LeadContactCreate):
    db_contact = models.LeadContact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_lead_contacts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.LeadContact).offset(skip).limit(limit).all()

def get_lead_contact(db: Session, contact_id: int):
    return db.query(models.LeadContact).filter(models.LeadContact.id == contact_id).first()

def update_lead_contact(db: Session, contact_id: int, contact: schemas.LeadContactUpdate):
    # Get the existing contact to be updated
    db_contact = db.query(models.LeadContact).filter(models.LeadContact.id == contact_id).first()
    
    if not db_contact:
        return None  # If the contact doesn't exist, return None

    # Update fields (add more fields as necessary)
    for key, value in contact.dict(exclude_unset=True).items():
        setattr(db_contact, key, value)
    
    db.commit()  # Commit the changes to the database
    db.refresh(db_contact)  # Refresh the instance with the updated data
    return db_contact

def delete_lead_contact(db: Session, contact_id: int):
    # Query to find the lead contact by its ID
    db_contact = db.query(models.LeadContact).filter(models.LeadContact.id == contact_id).first()
    
    if not db_contact:
        return False  # Return False if the contact doesn't exist

    db.delete(db_contact)  # Delete the found contact
    db.commit()  # Commit the deletion to the database
    return True  # Return True to indicate successful deletion

# CRUD operations for Interactions
def create_interaction(db: Session, interaction: schemas.InteractionCreate):
    db_interaction = models.Interaction(**interaction.dict())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

def get_interactions(db: Session, skip: int = 0, limit: int = 10):
    interactions = db.query(models.Interaction).offset(skip).limit(limit).all()
    print(interactions)  # Check the interactions
    return interactions

def get_interaction(db: Session, interaction_id: int):
    return db.query(models.Interaction).filter(models.Interaction.id == interaction_id).first()

def update_interaction(db: Session, interaction_id: int, interaction: InteractionUpdate):
    # Fetch the existing interaction from the database
    db_interaction = db.query(models.Interaction).filter(models.Interaction.id == interaction_id).first()
    
    if not db_interaction:
        return None

    # Update the fields
    if interaction.type:
        db_interaction.type = interaction.type
    if interaction.note:
        db_interaction.note = interaction.note
    if interaction.is_active is not None:
        db_interaction.is_active = interaction.is_active

    # Commit the changes to the database
    db.commit()
    db.refresh(db_interaction)

    return db_interaction

def delete_interaction(db: Session, interaction_id: int):
    db_interaction = db.query(models.Interaction).filter(models.Interaction.id == interaction_id).first()
    if not db_interaction:
        return False
    
    db.delete(db_interaction)
    db.commit()
    return True

# CRUD operations for Performance
def create_performance(db: Session, performance: schemas.PerformanceCreate):
    # Check if the employee exists
    employee = db.query(models.Employee).filter(models.Employee.id == performance.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Proceed with inserting the performance record
    db_performance = models.Performance(**performance.dict())
    db.add(db_performance)
    db.commit()
    db.refresh(db_performance)
    return db_performance

def get_performances(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Performance).offset(skip).limit(limit).all()

def get_performance(db: Session, performance_id: int):
    return db.query(models.Performance).filter(models.Performance.id == performance_id).first()

def update_performance(db: Session, performance_id: int, performance: schemas.PerformanceUpdate):
    db_performance = db.query(models.Performance).filter(models.Performance.id == performance_id).first()
    if db_performance:
        for key, value in performance.dict(exclude_unset=True).items():
            setattr(db_performance, key, value)
        db.commit()
        db.refresh(db_performance)
        return db_performance
    return None

def delete_performance(db: Session, performance_id: int):
    db_performance = db.query(models.Performance).filter(models.Performance.id == performance_id).first()
    if db_performance:
        db.delete(db_performance)
        db.commit()
        return True
    return False

def get_performance_by_employee(db: Session, employee_id: int):
    return db.query(models.Performance).filter(models.Performance.employee_id == employee_id).all()

# CRUD operations for Employees
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        for var, value in vars(employee).items():
            setattr(db_employee, var, value) if value else None
        db.commit()
        db.refresh(db_employee)
        return db_employee
    return None

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
        return True
    return False