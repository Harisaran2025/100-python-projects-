import json
import os
TASK_FILE='tasks.json'
if not os.path.exists(TASK_FILE):
  with open(TASK_FILE,'w') as file:
    json.dump([],file)
#step1 load tasks
def load_tasks():
  with open(TASK_FILE,'r') as file:
    tasks = json.load(file)
    changed = False
    for task in tasks:
      if 'Status:' in task and 'Status: ' not in task: 
        task['Status: '] = task.pop('Status:') 
        changed = True
    if changed:
        save_tasks(tasks) 
    return tasks
#step 2 save tasks
def save_tasks(tasks):
  with open(TASK_FILE,'w') as file:
    json.dump(tasks,file,indent=2)
#step 3 add tasks
def add_task():
  task_name=input("Enter the task name: ").strip()
  tasks=load_tasks()
  tasks.append({"Task: ":task_name,"Status: ":"Incomplete"}) 
  save_tasks(tasks)
  print(f"Task '{task_name}' added successfully")
#step4 view tasks
def view_tasks():
  tasks=load_tasks()
  if tasks:
    print("\n---Task List---")
    for index,task in enumerate(tasks,start=1):
      print(f"{index}. {task['Task: ']} - {task['Status: ']}") 
  else:
    print("No tasks found")

#step 5 update tasks
def update_task():
  tasks=load_tasks()
  view_tasks()
  try:
    task_index=int(input("Enter the task number to update: "))-1
    if 0<=task_index<len(tasks):
      new_status=input("Enter the new status(Complete/Incomplete): ").strip()
      tasks[task_index]['Status: '] = new_status 
      save_tasks(tasks)
      print("Task updated successfully")
    else:
      print("Invalid task number")
  except ValueError:
    print("Invalid input. Please enter a valid task number")

#step 6 delete task
def delete_task():
  tasks=load_tasks()
  view_tasks()
  try:
    task_index=int(input("Enter the task number to delete: "))-1
    if 0<=task_index<len(tasks):
      deleted_task=tasks.pop(task_index)
      save_tasks(tasks)
      print(f"Task '{deleted_task['Task: ']}' deleted successfully")
    else:
      print("Invalid task number")
  except ValueError:
    print("Invalid input. Please enter a valid task number")

#step 7 main program
def show_menu():
  print("\n---Task Manager---")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Update Task")
  print("4. Delete Task")
  print("5. Exit")

while True:
  show_menu()
  choice=input("Enter your choice(1/2/3/4/5): ")
  if choice=='1':
    add_task()
  elif choice=='2':
    view_tasks()
  elif choice=='3':
    update_task()
  elif choice=='4':
    delete_task()
  elif choice=='5':
    print("Thankyou for using!")
    break
  else:
    print("Invalid choice. Please try again")
