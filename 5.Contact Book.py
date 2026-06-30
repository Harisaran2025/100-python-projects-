#contact book
contacts={}
def show_menu():
  print("\n-----Contact Book Menu-----")
  print("1. Add contact")
  print("2. Remove contact")
  print("3. View contacts")
  print("4. Search contact")
  print("5. Edit contacts")
  print("6. Exit")

def add_contact():
  name=input("Enter the name: ")
  phone=input("Enter the phone number: ")
  email=input("Enter the email: ")
  contacts[name]={"Phone":phone,"Email":email}
  print(f"{name} has been added to the contact book.")
def remove_contact():
  name=input("Enter the name: ")
  if name in contacts:
    del contacts[name]
    print(f"{name} has been removed from the contact book.")
  else:
    print(f"{name} is not in the contact book.")
def view_contacts():
  print("\n-----Contacts list-----")
  if not contacts:
    print("The contact book is empty.")
  else:
    for name,info in contacts.items():
      print(f"\nName: {name}")
      print(f"Phone: {info['Phone']}")
      print(f"Email: {info['Email']}")
def search_contact():
  name=input("Enter the name of contact to search: ")
  if name in contacts:
    info=contacts[name]
    print(f"\nName: {name}")
    print(f"Phone: {info['Phone']}")
    print(f"Email: {info['Email']}")
  else:
    print(f"{name} is not in the contact book.")
def edit_contact():
  name=input("Enter the name of contact to edit: ")
  if name in contacts:
    phone=input("Enter the new phone number: ")
    email=input("Enter the new email: ")
    contacts[name]={"Phone":phone,"Email":email}
    print(f"{name}'s information has been updated.")
  else:
    print(f"{name} is not in the contact book.")
while True:
  show_menu()
  choice=input("Enter your choice (1-6): ")
  if choice=="1":
    add_contact()
  elif choice=="2":
    remove_contact()
  elif choice=="3":
    view_contacts()
  elif choice=="4":
    search_contact()
  elif choice=="5":
    edit_contact()
  elif choice=="6":
    print("Thankyou for usig the Contact Book")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 6.")
