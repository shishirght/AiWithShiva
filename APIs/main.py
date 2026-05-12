# import FastAPI
# FastAPI is the predefined class, used to develop API Calls
from fastapi import FastAPI

# import BaseModel
# BaseModel used to define Schema
from pydantic import BaseModel


# instantiate FastAPI
app = FastAPI()

# Define Schema (Rules & Regulations)
class Employee(BaseModel):
    emp_id:int
    emp_name:str
    department:str
    salary:float
    experience:int
    email:str
    is_active:bool


employees = [{
     "emp_id":111,
     "emp_name":"Emp1",
     "department":"CSE",
     "salary":10000,
     "experience":1,
     "email":"emp1@gmail.com",
     "is_active":True
    },
    {
     "emp_id":222,
     "emp_name":"Emp2",
     "department":"ECE",
     "salary":20000,
     "experience":2,
     "email":"emp2@gmail.com",
     "is_active":True
    },
    {
     "emp_id":333,
     "emp_name":"Emp3",
     "department":"MECH",
     "salary":30000,
     "experience":3,
     "email":"emp3@gmail.com",
     "is_active":True
    }]

#swaggwr http://127.0.0.1:8000/docs
#swaggwr http://127.0.0.1:8000/redoc
#

@app.get("/")
def home():
    return {"message":"Welcome to Fast API"}

@app.get("/employees")
def get_employees():
    return employees

#req parameter
@app.get("/employee/{emp_id}")
def get_employee(emp_id:int):
    for emp in employees:
        if emp["emp_id"] == emp_id:
            return emp
    return {"message":"Employee not found"}

@app.post("/add-employee")
def add_employee(employee:Employee):
    employees.append(employee.dict())
    return {"message":"Employee added successfully"}    

@app.put("/update-employee/{emp_id}")
def update_employee(emp_id:int, employee:Employee):
    for emp in employees:
        if emp["emp_id"] == emp_id:
            emp.update(employee.dict())
            return {"message":"Employee updated successfully"}
    return {"message":"Employee not found"}

@app.delete("/delete-employee/{emp_id}")
def delete_employee(emp_id:int):
    for emp in employees:
        if emp["emp_id"] == emp_id:
            employees.remove(emp)
            return {"message":"Employee deleted successfully"}
    return {"message":"Employee not found"}