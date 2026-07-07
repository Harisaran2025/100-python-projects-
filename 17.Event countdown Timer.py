#Event Countdown Timer
from datetime import datetime
import time
def get_event_datetime():
  try:
    date_input = input("Enter the event date(YYYY-MM-DD HH:MM:SS): ")
    return datetime.strptime(date_input,'%Y-%m-%d %H:%M:%S')
  except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS format")
    return None

def calculate_time_remaining(event_time):
  current_time=datetime.now()
  time_difference=event_time-current_time
  return time_difference

def display_countdown(time_left):
  days=time_left.days
  hours,renainder=divmod(time_left.seconds,3600)
  minutes,seconds=divmod(renainder,60)
  print(f"\nTime remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds",end="")
def start_countdown(vent_date):
  while True:
    time_left=calculate_time_remaining(vent_date)
    if time_left.total_seconds()<=0:
      print("\nEvent has already passed")
      break
    display_countdown(time_left)
    time.sleep(1)

event_date=get_event_datetime()
if event_date:
  print(f"Event set for : {event_date}")
  start_countdown(event_date)
