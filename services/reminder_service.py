class ReminderService:

    def __init__(self):
        self.reminders = []

    def create_reminder(self, reminder):

        self.reminders.append(reminder)
        return reminder

    def get_reminders(self):
        return self.reminders
