class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        return "Email Notification Sent"

class SMSNotification(Notification):
    def send(self):
        return "SMS Notification Sent"
