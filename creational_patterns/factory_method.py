class PaymentProcessor:
    def process(self):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process(self):
        return "Processing Credit Card"

class PayPalProcessor(PaymentProcessor):
    def process(self):
        return "Processing PayPal"
