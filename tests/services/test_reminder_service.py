from services.reminder_service import ReminderService

def test_create_reminder():

    service = ReminderService()

    reminder = {
        "message": "Study"
    }

    result = service.create_reminder(reminder)

    assert result["message"] == "Study"
