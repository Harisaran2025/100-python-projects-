import time
st=int(input("Enter the number to start the countdown from : "))
print("\n-----Countdown Begins-----")
while st>0:
  print(st)
  time.sleep(1)
  st-=1
  if st==0:
    print("-----Countdown Ends-----")
