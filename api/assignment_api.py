from fastapi import FastAPI
from services.assignment_service import AssignmentService
from src.assignment import Assignment

app = FastAPI()

assignment_service = AssignmentService()

@app.get("/api/assignments")
def get_assignments():
    return assignment_service.get_all_assignments() 
