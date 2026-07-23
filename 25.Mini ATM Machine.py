class BankAccount:
  def __init__(self,account_number,pin,balance):
    self.account_number=account_number
    self.__pin=pin
    self.__balance=balance
#pin validation
  def validate_pin(self,entered_pin):
    return entered_pin == self.__pin
#balance check
  def get_balance(self):
    print(f"Current Balance: {self.__balance}")
#deposit amount
  def deposit(self,amount):
    if amount > 0:
      self.__balance += amount
      print(f"Deposited {amount}. New Balance: {self.__balance}")
      print(f"Current Balance: {self.__balance}")
    else:
      print("Invalid deposit amount")
#withdraw amount
  def withdraw(self,amount):
    if amount>self.__balance:
      print("Insufficient funds")
    elif amount>0:
      self.__balance -= amount
      print(f"Withdrew {amount}. New Balance: {self.__balance}")
      print(f"Current Balance: {self.__balance}")
    else:
      print("Invalid withdrawal amount")
#atm pin change
  def change_pin(self,old_pin,new_pin):
    if self.validate_pin(old_pin) and len(new_pin)==4 and new_pin.isdigit():
      self.__pin = new_pin
      print("PIN changed successfully")
    else:
      print("Failed to Change pin. Invalid old PIN")

class ATM:
  def __init__(self,):
    self.accounts={}
# creating an bank account
  def create_account(self):
    account_number = input("Enter account number: ").strip()
    pin = input("Enter a 4 digit PIN: ").strip()
    if len(pin) == 4 and pin.isdigit():
      self.accounts[account_number] = BankAccount(account_number,pin,0) # Added initial balance of 0
      print("Account created successfully")
    else:
      print("Invalid PIN. PIN must be a 4 digit number")
#authentication the bank account
  def authenticate_account(self):
    account_number = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()
    account=self.accounts.get(account_number)
    if account and account.validate_pin(pin):
      print("Authentication successful")
      self.account_menu(account)
    else:
      print("Authentication failed")
#menu to access account options
  def account_menu(self,account):
    while True:
      print("\n-----ATM Menu-----")
      print("1. Check Balance")
      print("2. Deposit")
      print("3. Withdraw")
      print("4. Change PIN")
      print("5. Exit")
      choice = int(input("Enter your choice (1/2/3/4/5): ").strip())
      if choice == 1:
        account.get_balance() # Added parentheses to call the method
      elif choice == 2:
        amount = float(input("Enter deposit amount: ").strip())
        account.deposit(amount)
      elif choice == 3:
        amount = float(input("Enter withdrawal amount: ").strip())
        account.withdraw(amount)
      elif choice == 4:
        old_pin = input("Enter old PIN: ").strip()
        new_pin = input("Enter new PIN: ").strip()
        account.change_pin(old_pin,new_pin)
      elif choice ==5:
        print("Thank You for using our ATM")
        break
      else:
        print("Invalid choice")
#account entering main menu
  def main_menu(self):
    while True:
      print("\n----Welcome to mini ATM Machine----")
      print("1. Create Account")
      print("2. Authenticate Account")
      print("3. Exit")
      choice = int(input("Enter your choice (1/2/3): ").strip())
      if choice == 1:
        self.create_account()
      elif choice == 2:
        self.authenticate_account()
      elif choice == 3:
        print("Thankyou for using mini ATM")
        break
      else:
        print("Invalid choice")

if __name__=="__main__":
  atm =ATM()
  atm.main_menu()
