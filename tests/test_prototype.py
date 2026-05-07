from creational_patterns.prototype import AssignmentTemplate

def test_clone():
    a1 = AssignmentTemplate("Math Assignment")
    a2 = a1.clone()
    assert a1.title == a2.title
