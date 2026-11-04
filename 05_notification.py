class Notification:
    def send(self, message):
        print(f"Sending notification: {message}")


class EmailNotification(Notification):
    def send(self, message):
        print(f"[EMAIL] Sending email to inbox: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS] Sending text message to mobile: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"[PUSH] Sending app push alert: {message}")


for n in (EmailNotification(), SMSNotification(), PushNotification()):
    n.send("Your order has been shipped.")
