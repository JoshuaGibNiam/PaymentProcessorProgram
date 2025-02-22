from base import PaymentProcessor
class CryptoPayment(PaymentProcessor):
    def transaction_fee(self):
        return 0

    def wait_for_blockchain_confirmation(self):
        print("Waiting for blockchain confirmation....."
              "Transaction confirmed!")
    def generate_receipt(self):
        print("Receipt: Paid $XX.XX in cryptocurrency. \n"
              "TX Hash: 002cf51cf6ba48b4b4d0d02fe688e82cef112cbc4a6fc9d55e9b8759d2708eda")

    def process_payment(self):
        """Process blockchain confirmation before transaction"""
        print(f"Processing Paypal payment of {self.amount:.2f}...")
        self.wait_for_blockchain_confirmation()
        self.deposit_payment()
        self.generate_receipt()

if __name__ == "__main__":
    myclass = CryptoPayment(200)
    myclass.process_payment()
