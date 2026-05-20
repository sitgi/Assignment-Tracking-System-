
from services.user_service import UserService

def test_create_user():

    service = UserService()

    user = service.create_user(
        "John",
        "john@email.com"
    )

    assert user["name"] == "John"


def test_invalid_user():

    service = UserService()

    try:
        service.create_user("", "")
        assert False
    except ValueError:
        assert True
