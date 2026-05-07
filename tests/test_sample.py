from creational_patterns.simple_factory import AssignmentFactory

def test_assignment_factory():
    assignment = AssignmentFactory.create_assignment("homework")
    assert assignment.create() == "Homework Assignment Created"
