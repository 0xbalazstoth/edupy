# SOLID elvek:
# 1. Single Responsibility Principle (SRP)
# 2. Open/Closed Principle (OCP)
# 3. Liskov Substitution Principle (LSP)
# 4. Interface Segregation Principle (ISP)
# 5. Dependency Inversion Principle (DIP)
from abc import ABC, abstractmethod


# Bad practice
# A kód a konkrét implementációktól függ, nem pedig az absztrakciótól.
class EmailSender:
    def send(self, message: str):
        print(f"Sending email: {message}")


class SmsSender:
    def send(self, message: str):
        print(f"Sending SMS: {message}")


class MessageService:
    def __init__(self, sender_type: str):
        if sender_type == "email":
            self.message_sender = EmailSender()
        elif sender_type == "sms":
            self.message_sender = SmsSender()
        else:
            raise ValueError("Invalid sender type")

    def send_message(self, message: str):
        self.message_sender.send(message)


# Használat
notification_service = MessageService("email")
notification_service.send_message("Hello World!")

notification_service = MessageService("sms")
notification_service.send_message("Hello World!")


# Dependency Inversion Principle (DIP) - Függőség megfordításának elve
# - A kód függjön az absztrakcióktól, ne a konkrét implementációktól.
# Javított változat
class MessageSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailSender(MessageSender):
    def send(self, message: str):
        print(f"Sending email: {message}")


class SmsSender(MessageSender):
    def send(self, message: str):
        print(f"Sending SMS: {message}")


class MessageService:
    def __init__(self, message_sender: MessageSender):
        self.message_sender = message_sender

    def send_message(self, message: str):
        self.message_sender.send(message)


email_sender = EmailSender()
notification_service = MessageService(email_sender)
notification_service.send_message("Hello World!")

sms_sender = SmsSender()
notification_service = MessageService(sms_sender)
notification_service.send_message("Hello World!")
