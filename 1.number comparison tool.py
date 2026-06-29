# number comparison tool
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
print("\n----Comparison Results----")
if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")
if num1==0 and num2==0:
  print("\nBoth of given number is zero.")
else:
  print("\nAny one of given number is zero.")
