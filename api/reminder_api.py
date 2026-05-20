from fastapi import FastAPI
from services.reminder_service import ReminderService

app = FastAPI()

reminder_service = ReminderService()

@app.get("/api/reminders")
def get_reminders():
    return reminder_service.get_reminders()
