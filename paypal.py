from base import PaymentProcessor


class PayPal(PaymentProcessor):
    """represents PayPal payment. Charges flat fee of 1.5$"""

    def validate_paypal_account(self):
        print("Finding paypal account...")
        print("Account validated!")

    def process_payment(self):
        """Performs an account validation before transaction"""
        print(f"Processing Paypal payment of {self.amount:.2f}...")
        self.validate_paypal_account()
        self.deposit_payment()
        self.generate_receipt()

    def transaction_fee(self):
        """Charges flat fee of $1.5 per payment"""
        return self.amount + 1.5

    def generate_receipt(self):
        print(f"Transaction made by PayPal payment: \n"
              f"payment of ${self.amount:.2f} deposited to merchant account.\n"
              f"Transaction fee: ${self.transaction_fee()}")
