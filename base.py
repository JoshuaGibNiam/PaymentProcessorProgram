from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    total_balance = 0  # Shared repository for all deposits

    def __init__(self, amount):
        self.__amount = amount
        self.__confirmed = False  # Tracks payment confirmation

    @property
    def amount(self):
        """Returns the transaction amount."""
        return self.__amount

    @amount.setter
    def amount(self, value):
        """Ensures the amount is always positive and is an integer and returns True if so."""
        if value <= 0:
            raise ValueError("Transaction amount must be positive!")
        if type(value) != int:
            raise TypeError("Transaction amount must be an integer!")
        self.__amount = value


    @property
    def confirmed(self):
        """Returns payment confirmation status."""
        return self.__confirmed

    @confirmed.setter
    def confirmed(self, value):
        """Allows setting confirmation status only to True."""
        if not isinstance(value, bool):
            raise ValueError("Confirmation must be True or False.")
        self.__confirmed = value

    @confirmed.deleter
    def confirmed(self):
        """Cancels the payment by resetting the amount to zero."""
        print("🚨 Payment canceled. Amount reset to $0.00.")
        self.__amount = 0

    @abstractmethod
    def process_payment(self):
        """Each payment method must define how it processes payments."""
        pass

    @abstractmethod
    def transaction_fee(self):
        """Each payment method must define its own fee structure."""
        pass

    @abstractmethod
    def generate_receipt(self):
        """Each payment method generates a different type of receipt."""
        pass

    def deposit_payment(self):
        """Finalizes payment by adding net amount (after fees) to total balance."""
        if not self.confirmed:
            confirm = input(f"Confirm payment of ${self.amount:.2f}? (yes/no): ").strip().lower()
            if confirm == "yes":
                self.confirmed = True
            else:
                del self.confirmed  # 🚨 Payment gets canceled!
                return

        net_amount = self.amount - self.transaction_fee()
        PaymentProcessor.total_balance += net_amount
        print(f"✅ Payment confirmed! Deposited ${net_amount:.2f} into merchant account. "
              f"Total balance: ${PaymentProcessor.total_balance:.2f}")
