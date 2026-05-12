from repositories.inmemory.inmemory_assignment_repository import InMemoryAssignmentRepository
from src.assignment import Assignment

def test_save_assignment():

    repo = InMemoryAssignmentRepository()

    assignment = Assignment(
        1,
        "Math Assignment",
        "2026-06-01"
    )

    repo.save(assignment)

    assert repo.find_by_id(1) == assignment


def test_delete_assignment():

    repo = InMemoryAssignmentRepository()

    assignment = Assignment(
        1,
        "Math Assignment",
        "2026-06-01"
    )

    repo.save(assignment)
    repo.delete(1)

    assert repo.find_by_id(1) is None
