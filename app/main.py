# app/main.py
from fastapi import FastAPI
from app.api import leads, lead_contacts, interactions, performances, employees

app = FastAPI()

app.include_router(leads.router, tags=["Leads"])
app.include_router(lead_contacts.router, tags=["Lead Contacts"])
app.include_router(interactions.router, tags=["Interactions"])
app.include_router(performances.router, tags=["Performances"])
app.include_router(employees.router, tags=["Employees"])

@app.on_event("startup")
async def startup():
    from app.db import recreate_database
    recreate_database()
