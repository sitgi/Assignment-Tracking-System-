from services.assignment_service import AssignmentService
from src.assignment import Assignment

def test_create_assignment():

    service = AssignmentService()

    assignment = Assignment(
        1,
        "Math",
        "2026-06-01"
    )

    result = service.create_assignment(assignment)

    assert result.title == "Math"
