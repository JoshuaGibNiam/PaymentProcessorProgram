from base import PaymentProcessor


class CreditCardPayment(PaymentProcessor):
    """
       Represents a credit card payment.
       Implements the abstract methods from PaymentProcessor.
       """

    # fraud_check method
    def fraud_check(self):
        print("Performing fraud check.... Fraud check complete!")

    def process_payment(self):
        """
               Handles the credit card payment process.
               Performs a fraud check before confirming and depositing payment.
               """
        print(f"Processing credit card payment of {self.amount:.2f}.")
        self.fraud_check()
        self.deposit_payment()
        self.generate_receipt()

    # transaction_fee
    def transaction_fee(self):
        """
                Returns the transaction fee for credit card payments.
                Credit cards charge a 3% fee on the total amount.
                """
        return self.amount * 0.03

    def generate_receipt(self):
        print(f"Transaction made for credit card payment: {self.amount - self.transaction_fee():.2f}"
              f"deposited into account. Transaction fee: {self.transaction_fee():.2f}.")