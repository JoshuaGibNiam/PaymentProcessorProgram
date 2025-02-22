from base import PaymentProcessor
from credit_card import CreditCardPayment
from paypal import PayPal
from crypto_payment import CryptoPayment


payments = [
    CreditCardPayment(100),
    PayPal(50),
    CryptoPayment(200)
    ]
for payment in payments:
    payment.process_payment()
    print("-" * 50)
print(f"\nFinal Merchant Account Balance: ${PaymentProcessor.total_balance:.2f}")