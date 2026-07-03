#13
# Daily Journal Logger
#step 1
JOURNAL_FILE='journal.txt'
#step 2
def add_entry():
  entry= input("Write your journal entry: ")
  with open(JOURNAL_FILE,'a') as file:
    file.write(entry+'\n')
    print("Entry added successfully")
#step 3
def view_entries():
  try:
    with open(JOURNAL_FILE,'r') as file:
      content=file.read()
      if content:
        print("No entries found")
        print("\n---Journal Entries---")
        print(content)
      else:
        print("No entries found . Start Writing Today")
  except FileNotFoundError:
    print("No journal file found. add an empty first!")

#step 4
def search_entries():
  keyword=input("Enter the search term: ").strip().lower()
  try:
    with open(JOURNAL_FILE,'r') as file:
      content=file.read().lower()
      found= False
      print("\n---Search Results---")
      for entry in entries:
        if keyword in entry.lower():
          print(entry.strip())
          found=True
      if not found:
        print("No matching entries found")
  except FileNotFoundError:
    print("No journal file found. add an empty first!")
        
#step 5
def show_menu():
  print("\n---Daily Journal Logger---")
  print("1. Add Entry")
  print("2. View Entries")
  print("3. Search Entries by keyword")
  print("4. Exit")

#step 6
while True:
  show_menu()
  choice=input("Enter your choice(1/2/3/4): ")
  if choice=='1':
    add_entry()
  elif choice=='2':
    view_entries()
  elif choice=='3':
    search_entries()
  elif choice=='4':
    print("Thankyou for using!")
    break
  else:
    print("Invalid choice. Please try again")
