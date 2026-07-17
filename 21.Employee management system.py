#Employee management system
from os import name
class Employeee:
    def __init__(self,name,id,salary):
      self.name=name
      self.id=id
      self.salary=salary
    def display(self):
      print("\n-----Employee Details-----")
      print(f"Name: {self.name}")
      print(f"ID: {self.id}")
      print(f"Salary: {self.salary}")

    def calculate_bonus(self):
      return self.salary*0.1

class Manager(Employeee):
  def __init__(self,name,id,salary,department):
    super().__init__(name,id,salary)
    self.department=department

  def display(self):
    super().display()
    print(f"Department: {self.department}")

  def calculte_bonus(self):
    return self.salary*0.2

class Developer(Employeee):
  def __init__(self,name,id,salary,programming_language):
    super().__init__(name,id,salary)
    self.programming_language=programming_language

  def display(self):
    return super().display()
    print(f"Programming Language: {self.programming_language}")

  def calculate_bonus(self):
    return self.salary*0.15

employees = []

def add_employee():
  print("\n----Choose Emploee Type----")
  print("1. Manager")
  print("2. Developer")
  print("3. Employee")
  choice = int(input("Enter your choice (1/2): ").strip())
  name = input("Enter employee name: ").strip()
  id = input("Enter employee ID: ").strip()
  salary = float(input("Enter employee salary: ").strip())
  
  if choice == 1:
    department = input("Enter department: ").strip()
    employees.append(Manager(name,id,salary,department))
  elif choice == 2:
    programming_language = input("Enter programming language: ").strip()
    employees.append(Developer(name,id,salary,programming_language))
  elif choice == 3:
    employees.append(Employeee(name,id,salary))
  else:
    print("Invalid choice")

def display_employees():
  print("\n-----Employee List-----")
  for employee in employees:
    employee.display()
    print(f"Bonus: {employee.calculate_bonus()}")
    print("------------------------")

while True:
  print("\n-----Employee Management System-----")
  print("1. Add Employee")
  print("2. Display Employees")
  print("3. Exit")
  choice = int(input("Enter your choice (1/2/3): ").strip())
  if choice == 1:
    add_employee()
  elif choice == 2:
    display_employees()
  elif choice == 3:
    print("Exiting Employee Management System")
    break
  else:
    print("Invalid choice")


