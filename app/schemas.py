# app/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from datetime import datetime

# Lead Schema
class LeadBase(BaseModel):
    name: str
    status: str
    is_active: Optional[bool] = True

class LeadCreate(LeadBase):
    pass

class Lead(LeadBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# LeadContact Schema

class LeadContact(BaseModel):
    id: int
    lead_id: int  # Ensure lead_id is an integer here
    created_at: datetime

    class Config:
        orm_mode = True

class LeadContactBase(BaseModel):
    email: str
    phone: str

class LeadContactCreate(LeadContactBase):
    lead_id: int

class LeadContact(LeadContactBase):
    id: int
    lead_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class LeadContactUpdate(LeadContactBase):
    pass

class LeadContactResponse(BaseModel):
    id: int
    lead_id: int
    email: str
    phone: str
    created_at: datetime

    class Config:
        orm_mode = True

# Interaction Schema
class InteractionBase(BaseModel):
    type: str
    note: Optional[str] = None
    is_active: Optional[bool] = True

# class InteractionCreate(InteractionBase):
#     lead_id: int

class InteractionCreate(InteractionBase):
    lead_id: int  # Ensure this field is required and passed in the request data
    type: str
    note: str

# Schema for updating an interaction
class InteractionUpdate(InteractionBase):
    pass

class Interaction(InteractionBase):
    id: int
    lead_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Performance Schema
class PerformanceBase(BaseModel):
    target_achieved: int
    performance_review: str

class PerformanceCreate(PerformanceBase):
    employee_id: int
    lead_id: int

class Performance(PerformanceBase):
    id: int
    employee_id: int
    lead_id: int

    class Config:
        orm_mode = True

# Employee Schema
class EmployeeBase(BaseModel):
    name: str
    role: str
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Shared attributes for leads
class LeadBase(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = True

# Schema for creating a lead
class LeadCreate(LeadBase):
    name: str
    status: str

# Schema for updating a lead
class LeadUpdate(LeadBase):
    pass

# Schema for reading a lead
class Lead(BaseModel):
    id: int
    name: str
    status: str
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        orm_mode = True

# Similarly, define Update schemas for other entities

class EmployeeBase(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    department: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    name: str
    role: str
    department: str

class EmployeeUpdate(EmployeeBase):
    pass

class Employee(BaseModel):
    id: int
    name: str
    role: str
    department: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class PerformanceBase(BaseModel):
    employee_id: Optional[int] = None
    lead_id: Optional[int] = None
    target_achieved: Optional[int] = None
    performance_review: Optional[str] = None

class PerformanceCreate(PerformanceBase):
    employee_id: int
    lead_id: int
    target_achieved: int
    performance_review: str

class PerformanceUpdate(PerformanceBase):
    pass

class Performance(BaseModel):
    id: int
    employee_id: int
    lead_id: int
    target_achieved: int
    performance_review: str

    class Config:
        orm_mode = True
