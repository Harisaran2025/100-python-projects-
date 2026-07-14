#Bank Account Simulator
class BankAccount:
  def __init__(self,account_number,account_holder,balance=0.0):
    self.account_number=account_number
    self.account_holder=account_holder
    self.balance=balance
  #Deposit Money
  def deposit(self,amount):
    if amount>0:
      self.balance+=amount
      print(f"Deposited ${amount}. New balance: ${self.balance}")
    else:
      print("Invalid deposit amount. Amount must be greater than 0.")
    
  #Withdraw Money
  def withdraw(self,amount):
    if amount>0 and amount<=self.balance:
      self.balance-=amount
      print(f"Withdrew ${amount}. New balance: ${self.balance}")
    else:
      print("Invalid withdrawal amount or insufficient balance.")

  #Show Account Details
  def show_details(self):
    print("\n---Account Details---")
    print(f"Account Number: {self.account_number}")
    print(f"Account Holder: {self.account_holder}")
    print(f"Account Balance: ${self.balance}")
#Main Program
accounts={}

def create_account():
  account_number=input("Enter the account number: ").strip()
  account_holder=input("Enter the account holder name: ").strip()
  initial_deposit=float(input("Enter Initial Deposit Amount: "))
  account=BankAccount(account_number,account_holder,initial_deposit)
  accounts[account_number]=account
  print("Account created successfully")
  
def access_account():
  account_number=input("Enter the account number: ").strip()
  if account_number in accounts:
    account=accounts[account_number]
    while True:
      print("\n---Account Menu---")
      print("1. Deposit")
      print("2. Withdraw")
      print("3. Show Details")
      print("4. Exit")
      choice=input("Enter your choice(1/2/3/4): ")
      if choice=='1':
        amount=float(input("Enter the deposit amount: "))
        account.deposit(amount)
      elif choice=='2':
        amount=float(input("Enter the withdrawal amount: "))
        account.withdraw(amount)
      elif choice=='3':
        account.show_details()
      elif choice=='4':
        print("Thankyou for using!")
        break
      else:
        print("Invalid choice. Please try again")
  else:
    print("Account not found. Please create an account first")
#Main menu
while True:
  print("\n---Bank Account Simulator---")
  print("1. Create Account")
  print("2. Access Account")
  print("3. Exit")
  choice=input("Enter your choice(1/2/3): ")
  if choice=='1':
    create_account()
  elif choice=='2':
    access_account()
  elif choice=='3':
    print("Thankyou for using!")
    break
  else:
    print("Invalid choice. Please try again")
  
