# Lead Management System

This project is a **Lead Management System** designed for Key Account Managers (KAMs) to manage and track leads, employees, and performance records. The system uses **FastAPI**, **SQLAlchemy**, and **SQLite** for database interactions.

## Features

- **Leads Management**: Create, read, update, and delete leads.
- **Employee Management**: Manage employee records, including role, department, and performance.
- **Performance Tracking**: Track employee performance based on their target achievements and reviews.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: ORM (Object Relational Mapper) for database interactions.
- **SQLite**: Lightweight database for development and testing.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Installation

### Step 1: Clone the repository 

```bash
git clone https://github.com/Shubham-com/KAM-Tool.git
cd lead-management-system

### Step 2: Create and activate a virtual environment

#### Using Anaconda (optional but recommended for managing environments)

```bash
conda create -n LeadManagementSystem python=3.9
conda activate LeadManagementSystem

### Step 2: Create and activate a virtual environment

#### Using `venv`

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

### Step 3: Install dependencies

```bash
pip install -r requirements.txt

### Step 4: Install dependencies
```bash
uvicorn app.main:app --reload

## API Endpoints

### Leads
- **Create a lead**: `POST /leads/`
- **Get all leads**: `GET /leads/`
- **Get a lead by ID**: `GET /leads/{lead_id}`
- **Update a lead**: `PUT /leads/{lead_id}`
- **Delete a lead**: `DELETE /leads/{lead_id}`

### Employees
- **Create an employee**: `POST /employees/`
- **Get all employees**: `GET /employees/`
- **Get an employee by ID**: `GET /employees/{employee_id}`
- **Update an employee**: `PUT /employees/{employee_id}`
- **Delete an employee**: `DELETE /employees/{employee_id}`

### Performances
- **Create a performance record**: `POST /performances/`
- **Get all performance records**: `GET /performances/`
- **Get a performance by ID**: `GET /performances/{performance_id}`
- **Update a performance record**: `PUT /performances/{performance_id}`
- **Delete a performance record**: `DELETE /performances/{performance_id}`


