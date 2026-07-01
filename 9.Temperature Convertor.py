#temperature convertor
#step1 defining conversion function
def celsius_to_fahrenheit(celsius):
  return (celsius*9/5)+32

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit-32)*5/9

def kelvin_to_celsius(kelvin):
  return kelvin-273.15

def celsius_to_kelvin(celsius):
  return celsius+273.15

def fahrenheit_to_kelvin(fahrenheit):
  return (fahrenheit - 32)*5/9 + 273.15
  
def kelvin_to_fahrenheit(kelvin):
  return (kelvin - 273.15) * 9/5 + 32
#step 2:dispkay the menu
def show_menu():
  print("\n-----Temperature Converter Menu-----")
  print("1. Celsius to Fahrenheit & kelvin")
  print("2. Fahrenheit to Celsius & kelvin")
  print("3. Kelvin to Celsius & Fahrenheit")
  print("4. Exit")

#step 3: Main loop
while True:
  show_menu()
  choice=input("Enter your choice (1-4): ")
  if choice=="1":
    celsius=float(input("Enter temperature in Celsius: "))
    fahrenheit=celsius_to_fahrenheit(celsius)
    kelvin=celsius_to_kelvin(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K")
  elif choice=="2":
    fahrenheit=float(input("Enter temperature in Fahrenheit: "))
    celsius=fahrenheit_to_celsius(fahrenheit)
    kelvin=fahrenheit_to_kelvin(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K")
  elif choice=="3":
    kelvin=float(input("Enter temperature in Kelvin: "))
    celsius=kelvin_to_celsius(kelvin)
    fahrenheit=kelvin_to_fahrenheit(kelvin)
    print(f"{kelvin}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F")
  elif choice=="4":
    print("Thank you for using the Temperature Converter.")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 4.")
