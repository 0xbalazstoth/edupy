from abc import ABC, abstractmethod

# Absztrakt base osztály, amelynek egy absztrakt metódusa van
# Az absztrakt metódusoknak nincs implementációja (törzse), csak a szignatúrájuk van


class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


# Hitelkártyás fizetés osztály, amely örökli a Payment base osztályt
class CreditCardPayment(Payment):
    def __init__(self, card_number, cardholder_name, expiration_date):
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.expiration_date = expiration_date

    def process_payment(self, amount):
        return (
            f"Processing credit card payment of ${amount} for {self.cardholder_name}."
        )


# Paypal fizetés osztály, amely örökli a Payment base osztályt
class PaypalPayment(Payment):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount} for {self.email}."


# Objektumok létrehozása és a process_payment metódus meghívása
credit_card_payment = CreditCardPayment("1234567890123456", "John Doe", "12/25")
print(credit_card_payment.process_payment(100))

paypal_payment = PaypalPayment("john.doe@example.com")
print(paypal_payment.process_payment(200))
