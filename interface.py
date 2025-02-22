from base import PaymentProcessor
from credit_card import CreditCardPayment
from paypal import PayPal
from crypto_payment import CryptoPayment
class Interface():

    def main_menu(self) -> int:
        """Process main menu. Returns int for each action"""
        print("Enter a number to pay by:\n"
              "1. Credit Card\n"
              "2. PayPal\n"
              "3. Crypto Payment\n"
              "4. View merchant account balance\n"
              "5. Exit\n")

        action = input("Enter number: ")
        while not action.isdigit() and (not int(action) <= 4 and int(action) >= 1):
            action = input("Invalid action! PLease enter number: ")
        action = int(action)
        return action

    def credit_card(self):
        amount = input("Enter Amount: ")
        while not amount.isdigit() and amount > 0:
            amount = input("Invalid amount. Enter Amount: ")
        card = CreditCardPayment(int(amount))
        card.process_payment()

    def paypal(self):
        amount = input("Enter Amount: ")
        while not amount.isdigit() and amount > 0:
            amount = input("Invalid amount. Enter Amount: ")
        paypal = PayPal(int(amount))
        paypal.process_payment()

    def crypto_payment(self):
        amount = input("Enter Amount: ")
        while not amount.isdigit() and amount > 0:
            amount = input("Invalid amount. Enter Amount: ")
        crypto = CryptoPayment(int(amount))
        crypto.process_payment()

    def run(self):
        action = self.main_menu()
        if action == 1:
            self.credit_card()
        elif action == 2:
            self.paypal()
        elif action == 3:
            self.crypto_payment()
        elif action == 4:
            print(f"Merchant accoutn balance: ${PaymentProcessor.total_balance}")
        elif action == 5:
            return False
        return True