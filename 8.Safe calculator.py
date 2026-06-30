#step 1: define calculator function
def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  if y==0:
    raise ZeroDivisionError("Cannot divide by zero")
  return x/y
#step 2: display menu
def show_menu():
  print("\n-----Safe Calculator Menu-----")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. exit")
#step 3: main function
while True:
  show_menu()
  choice=input("Enter your choice (1-5): ")
  if choice=="5":
    print("Thank you for using the Safe Calculator.")
    break

  # Validate choice before asking for numbers
  if choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Please enter a number between 1 and 5.")
    continue

  num1 = None # Initialize variables to ensure they are defined
  num2 = None

  try:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
  except ValueError:
    print("Invalid input. Please enter valid numbers.")
    continue # Go back to the start of the while loop

  # Perform calculation after successful input
  try:
    if choice=="1":
      print("Result: ",add(num1,num2))
    elif choice=="2":
      print("Result: ",subtract(num1,num2))
    elif choice=="3":
      print("Result: ",multiply(num1,num2))
    elif choice=="4":
      try:
        print("Result: ",divide(num1,num2))
      except ZeroDivisionError as e:
        print(f"Error: {e}")
  except Exception as e:
    print(f"An unexpected error occurred during calculation: {e}")
