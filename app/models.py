# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.db import Base
import datetime


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)

    # Relationships
    contacts = relationship("LeadContact", back_populates="lead")
    interactions = relationship("Interaction", back_populates="lead")
    performances = relationship("Performance", back_populates="lead")


class LeadContact(Base):
    __tablename__ = "lead_contacts"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"),nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    lead = relationship("Lead", back_populates="contacts")


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"))
    type = Column(String, nullable=False)  # e.g., Email, Phone, Meeting
    note = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)  # Add this field if necessary

    # Relationships
    lead = relationship("Lead", back_populates="interactions")

    performance = relationship(
        "Performance",
        primaryjoin="Interaction.id == Performance.interaction_id",
        back_populates="interaction"
    )


class Performance(Base):
    __tablename__ = "performances"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    lead_id = Column(Integer, ForeignKey("leads.id"))
    interaction_id = Column(Integer, ForeignKey("interactions.id"))
    target_achieved = Column(Integer)
    performance_review = Column(String)

    # Relationships
    employee = relationship("Employee", back_populates="performances")
    lead = relationship("Lead", back_populates="performances")
    interaction = relationship(
        "Interaction",
        primaryjoin="Performance.interaction_id == Interaction.id",
        back_populates="performance"
    )


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)  # e.g., "Sales", "Manager"
    department = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    performances = relationship("Performance", back_populates="employee")
