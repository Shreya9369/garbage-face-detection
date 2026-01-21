
from twilio.rest import Client

class TwilioAlert:
    def __init__(self, account_sid, auth_token, twilio_number, contact_numbers):
        self.client = Client(account_sid, auth_token)
        self.twilio_number = twilio_number
        self.contact_numbers = contact_numbers
        self.messages_sent = {}

    def send_alert_if_needed(self, name):
        if name in self.contact_numbers and name not in self.messages_sent:
            message = self.client.messages.create(
                body=f"!!!ALERT!!!\n{name} has been detected. This is a warning notification from the garbage team.",
                from_=self.twilio_number,
                to=self.contact_numbers[name]
            )
            print(f"Message sent to {name}: {message.sid}")
            self.messages_sent[name] = True
