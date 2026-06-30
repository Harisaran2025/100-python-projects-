#shopping list app
shopping_list=[]
def show_menu():
  print("\n-----Shopping List Menu-----")
  print("1. Add item")
  print("2. Remove item")
  print("3. View list")
  print("4. Clear List")
  print("5. Quit")
while True:
  show_menu()
  choice=input("Enter your choice: ")
  if choice=="1":
    item=input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the list.")
  elif choice=="2":
    item=input("Enter the item to remove: ")
    if item in shopping_list:
      shopping_list.remove(item)
      print(f"{item} has been removed from the list.")
    else:
      print(f"{item} is not in the list.")
  elif choice=="3":
    print("\n-----Shopping List-----")
    if not shopping_list:
      print("The list is empty.")
    else:
      for index,item in enumerate(shopping_list,start=1):
        print(f"{index}. {item}")
  elif choice=="5":
    print("Goodbye!")
    break
  elif choice=="4":
    shopping_list.clear()
    print("The list has been cleared.")
