from twilio.rest import Client


TWILIO_SID = "YOUR_SID"
TWILIO_TOKEN = "YOUR_TOKEN"
TWILIO_NUMBER = "+17752589093"

CONTACTS = {
    "Shreya": "+919369149409",
    "Satish": "+918595984761"
}



class Messenger:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
        self.sent_messages = {}

    def send(self, name):
        if name in CONTACTS and name not in self.sent_messages:
            try:
                message = self.client.messages.create(
                    body=f"Alert! {name} detected near garbage.",
                    from_=TWILIO_NUMBER,
                    to=CONTACTS[name]
                )
                print(f"Message sent to {name}: {message.sid}")
                self.sent_messages[name] = True
            except Exception as e:
                print("Twilio error:", e)