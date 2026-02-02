import json
import hashlib
import os
from abc import ABC, abstractmethod
from datetime import datetime

DATABASE = "database.json"

# ---------- Custom Exceptions ----------
class UserAlreadyExistError(Exception): pass
class UserNotFound(Exception): pass
class AuthenticationError(Exception): pass
class InsufficientBalance(Exception): pass
class OverDraftLimit(Exception): pass


# ---------- Utility Functions ----------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_data():
    if not os.path.exists(DATABASE) or os.stat(DATABASE).st_size == 0:
        with open(DATABASE, "w") as file:
            json.dump({"users": [], "accounts": [], "transactions": []},file, indent=4)

    with open(DATABASE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATABASE, "w") as file:
        json.dump(data, file, indent=4)


def generate_id(data_list, key):
    if not data_list:
        return 1
    return max(item[key] for item in data_list) + 1


# ---------- User ----------
class User:

    def register(self):
        data_set = load_data()

        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        for user in data_set["users"]:
            if user["username"] == username:
                raise UserAlreadyExistError("User already exists")
        
        #User must select account type before registration
        print('Select Account Type')
        print('''1.Saving Account\n2.Current Account''')
        choice=input("Enter the Choice: ").strip()
        
        if choice=='1':
            account_type='saving'
        elif choice=='2':
            account_type='current'
        else:
            print("Invaild choices,default saving account")
            account_type='saving'
            
        #Automatically ID generated
        user_id = generate_id(data_set["users"], "user_id")
        account_id = generate_id(data_set["accounts"], "account_id")

        data_set["users"].append({
            "user_id": user_id,
            "username": username,
            "password": hash_password(password)
        })

        data_set["accounts"].append({
            "account_id": account_id,
            "user_id": user_id,
            "account_type": account_type,
            "balance": 0
        })

        save_data(data_set)
        print("Registration successful")


    def login(self):
        data_set = load_data()

        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        hashed = hash_password(password)

        for user in data_set["users"]:
            if user["username"] == username and user["password"] == hashed:
                print("Login successful")
                return user

        raise AuthenticationError("Invalid username or password")


# ---------- Account (Abstract) ----------
class Account(ABC):

    def __init__(self, account_data):
        self.account_id = account_data["account_id"]
        self.user_id = account_data["user_id"]
        self._balance = account_data["balance"]

    def save_balance(self):
        data_set = load_data()
        for acc in data_set["accounts"]:
            if acc["account_id"] == self.account_id:
                acc["balance"] = self._balance
        save_data(data_set)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")

        self._balance += amount
        self.save_balance()
        print("Amount deposited")

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingAccount(Account):

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        if self._balance < amount:
            raise InsufficientBalance("Not enough balance")

        self._balance -= amount
        self.save_balance()
        print("Withdraw successful (Saving)")


class CurrentAccount(Account):

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        if self._balance - amount < -500:
            raise OverDraftLimit("Overdraft limit exceeded")

        self._balance -= amount
        self.save_balance()
        print("Withdraw successful (Current)")


# ---------- Transactions ----------
class Transaction:

    def __init__(self, account_id, amount, t_type):
        self.data_set = load_data()

        txn_id = generate_id(self.data_set["transactions"], "transaction_id")

        self.data_set["transactions"].append({
            "transaction_id": txn_id,
            "account_id": account_id,
            "amount": amount,
            "type": t_type,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        save_data(self.data_set)

    @staticmethod
    def history():
        data_set = load_data()
        for t in data_set["transactions"]:
            print(t)


# ------------------- Banking Menu -------------------
def banking_system():
    current_user = None
    current_account = None

    while True:
        print("\n===== Welcome to My Bank =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                user = User() #object of user
                user.register()
            except UserAlreadyExistError as e:
                print(e)

        elif choice == "2":
            try:
                user = User()
                current_user = user.login()

                # Load user's account
                data_set= load_data()
                for acc in data_set["accounts"]:
                    
                    if acc["user_id"] == current_user["user_id"]:
                        if acc['account_type']=='saving':
                            current_account=SavingAccount(acc) #SavingAccount Object created 
                            
                        elif acc['account_type']=='current':
                            current_account=CurrentAccount(acc) #CurrentAccount Object Created
                            
                            break

                # User menu after login
                while True:
                    print(f"\nHello, {current_user['username']}! Choose operation:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Logout")
                    op = input("Enter choice: ").strip()

                    if op == "1":
                        try:
                            amount = float(input("Enter amount to deposit: "))
                            current_account.deposit(amount)
                            Transaction(current_account.account_id, amount, "deposit") #Transcation object created for deposit
                        except ValueError as e:
                            print(e)

                    elif op == "2":
                        try:
                            amount = float(input("Enter amount to withdraw: "))
                            current_account.withdraw(amount)
                        
                            Transaction(current_account.account_id, amount, "withdraw") #Transcation object created for withdraw
                        except (ValueError, InsufficientBalance, OverDraftLimit) as e:
                            print(e)

                    elif op == "3":
                        print(f"Current Balance: {current_account._balance}")

                    elif op == "4":
                        print("\n=== Transaction History ===")
                        data_set = load_data()
                        for t in data_set["transactions"]:
                            if t["account_id"] == current_account.account_id:
                                print(
                                    f"ID:{t['transaction_id']} | "
                                    f"Type:{t['type']} | "
                                    f"Amount:{t['amount']} | "
                                    f"Date:{t['date']}"
                                )

                    elif op == "5":
                        print("Logged out successfully.")
                        current_user = None
                        current_account = None
                        break
                    else:
                        print("Invalid choice!")

            except AuthenticationError as e:
                print(e)

        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid choice!")
            

# ---------- Run the banking system ----------
if __name__ == "__main__":
    banking_system()
