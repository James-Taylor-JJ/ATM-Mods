import json, logging, os
from account import Account

logging.basicConfig(filename='atm_log.txt', level=logging.INFO, format='%(asctime)s | %(message)s')
DATA_FILE = 'atm_data.json'

class OptionMenu:
    """Handles user interaction and menu navigation for the ATM."""

    def __init__(self):
        self._data = {}  # dict mapping customer_number (int) -> Account
        self._load_accounts()

    @staticmethod
    def _format_money(amount):
        return "${:,.2f}".format(amount)

    def _load_accounts(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r") as f:
            for d in json.load(f):
                acc = Account.from_dict(d)
                self._data[acc.get_customer_number()] = acc
 
    def _save_accounts(self):
        with open(DATA_FILE, "w") as f:
            json.dump([acc.to_dict() for acc in self._data.values()], f, indent=2)

    def _show_history(self, acc):
        transactions = acc.get_transactions()
        if not transactions:
            print("\nNo transactions on record.")
            return
        for i, t in enumerate(transactions, 1):
            print(f"\n  {i}. {t['time']} | {t['op']} | {t['account']} "
                  f"| {self._format_money(t['amount'])} | balance: {self._format_money(t['balance'])}")    

    # ------------------------------------------------------------------
    # Main Login Flow
    # ------------------------------------------------------------------

    def get_login(self):
        while True:
            try:
                customer_number = int(input("\nEnter your customer number: "))
                pin_number = int(input("\nEnter your PIN number: "))
                if customer_number in self._data:
                    acc = self._data[customer_number]
                    if pin_number == acc.get_pin_number():
                        self.get_account_type(acc)
                        return
                print("\nWrong Customer Number or Pin Number")
            except ValueError:
                print("\nInvalid Character(s). Only Numbers.")

    # ------------------------------------------------------------------
    # Select Account Type (Checking or Savings)
    # ------------------------------------------------------------------

    def get_account_type(self, acc):
        while True:
            try:
                print("\nSelect the account you want to access: ")
                print(" Type 1 - Checking Account")
                print(" Type 2 - Savings Account")
                print(" Type 3 - View Both Balances")
                print(" Type 4 - Exit")
                selection = int(input("\nChoice: "))
                if selection == 1:
                    self.get_checking(acc)
                elif selection == 2:
                    self.get_saving(acc)
                elif selection == 3:
                    self.get_both_balances(acc)
                elif selection == 4:
                    return
                else:
                    print("\nInvalid Choice.")
            except ValueError:
                print("\nInvalid Choice.")

    # ------------------------------------------------------------------
    # Checking Account Operations Menu
    # ------------------------------------------------------------------

    def get_checking(self, acc):
        while True:
            try:
                print("\nChecking Account: ")
                print(" Type 1 - View Balance")
                print(" Type 2 - Withdraw Funds")
                print(" Type 3 - Deposit Funds")
                print(" Type 4 - Transfer Funds")
                print(" Type 5 - View Transaction History")
                print(" Type 6 - Exit")
                selection = int(input("\nChoice: "))
                if selection == 1:
                    print("\nChecking Account Balance: " + self._format_money(acc.get_checking_balance()))
                elif selection == 2:
                    acc.get_checking_withdraw_input()
                    self._save_accounts()
                elif selection == 3:
                    acc.get_checking_deposit_input()
                    self._save_accounts()
                elif selection == 4:
                    acc.get_transfer_input("Checking")
                    self._save_accounts()
                elif selection == 5:
                    self._show_history(acc)
                elif selection == 6:
                    return
                else:
                    print("\nInvalid Choice.")
            except ValueError:
                print("\nInvalid Choice.")

    # ------------------------------------------------------------------
    # Savings Account Operations Menu
    # ------------------------------------------------------------------

    def get_saving(self, acc):
        while True:
            try:
                print("\nSavings Account: ")
                print(" Type 1 - View Balance")
                print(" Type 2 - Withdraw Funds")
                print(" Type 3 - Deposit Funds")
                print(" Type 4 - Transfer Funds")
                print(" Type 5 - View Transaction History")
                print(" Type 6 - Exit")
                selection = int(input("\nChoice: "))
                if selection == 1:
                    print("\nSavings Account Balance: " + self._format_money(acc.get_saving_balance()))
                elif selection == 2:
                    acc.get_saving_withdraw_input()
                    self._save_accounts()
                elif selection == 3:
                    acc.get_saving_deposit_input()
                    self._save_accounts()
                elif selection == 4:
                    acc.get_transfer_input("Savings")
                    self._save_accounts()
                elif selection == 5:
                    self._show_history(acc)
                elif selection == 6:
                    return
                else:
                    print("\nInvalid Choice.")
            except ValueError:
                print("\nInvalid Choice.")

    # ------------------------------------------------------------------
    # View Both Balances Operations Menu
    # ------------------------------------------------------------------

    def get_both_balances(self, acc):
        while True:
            try:
                print("\nSavings Account Balance: " + self._format_money(acc.get_saving_balance()))
                print("\nChecking Account Balance: " + self._format_money(acc.get_checking_balance()))
                print("\nType 1 - Exit")
                selection = int(input("\nChoice: "))
                if selection == 1:
                    return
                else:
                    print("\nInvalid Choice.")
            except ValueError:
                print("\nInvalid Choice.")

    # ------------------------------------------------------------------
    # Create New Account
    # ------------------------------------------------------------------

    def create_account(self):
        while True:
            try:
                cst_no = int(input("\nEnter your customer number "))
                if cst_no not in self._data:
                    break
                print("\nThis customer number is already registered")
            except ValueError:
                print("\nInvalid Choice.")

        try:
            pin = int(input("\nEnter PIN to be registered\n"))
        except ValueError:
            pin = 0

        self._data[cst_no] = Account(cst_no, pin)
        self._save_accounts()
        logging.info(f"New account created: Customer Number {cst_no}")
        print("\nYour new account has been successfully registered!")
        print("\nRedirecting to login.............")
        self.get_login()

    # ------------------------------------------------------------------
    # Main Menu Entry Point
    # ------------------------------------------------------------------

    def main_menu(self):
        self._load_accounts()
        # Pre-populated test accounts
        self._data[952141] = Account(952141, 191904, 1000, 5000)
        self._data[123] = Account(123, 123, 20000, 50000)
        self._save_accounts()

        while True:
            try:
                print("\n Type 1 - Login")
                print(" Type 2 - Create Account")
                choice = int(input("\nChoice: "))
                if choice == 1:
                    self.get_login()
                    break
                elif choice == 2:
                    self.create_account()
                    break
                else:
                    print("\nInvalid Choice.")
            except ValueError:
                print("\nInvalid Choice.")

        print("\nThank You for using this ATM.\n")
