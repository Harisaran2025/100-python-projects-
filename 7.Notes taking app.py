file_name="notes.txt"
def show_menu():
  print("\n-----Notes Taking App Menu-----")
  print("1. Add note")
  print("2. View notes")
  print("3. delete all notes")
  print("4. remove note")
  print("5. Quit")

def add_note():
  note=input("Enter your note: ")
  with open(file_name,"a") as file:
    file.write(note+"\n")
    print("Note added successfully.")

def view_notes():
    try:
      with open(file_name,"r") as file:
        notes=file.read()
        if notes:
          print("\n-----Notes-----")
          # Display notes with line numbers for easy reference
          for i, line in enumerate(notes.splitlines(), start=1):
            print(f"{i}. {line}")
        else:
          print("No notes found.")
    except FileNotFoundError:
      print("No notes file found. Please add a note first.")


def delete_all_notes():
  confirmation=input("Are you sure you want to delete all notes? (yes/no): ")
  if confirmation.lower()=="yes":
    with open(file_name,"w") as file:
      pass
    print("All notes have been deleted.")
  else:
    print("Notes deletion canceled.")

def remove_note():
  try:
    with open(file_name,"r") as file:
      lines=file.readlines()

    if not lines:
      print("No notes to remove.")
      return

    note_number=int(input("Enter the note number to remove: "))

    if 1<=note_number<=len(lines):
      del lines[note_number-1]
      with open(file_name,"w") as file:
        file.writelines(lines)
      print("Note removed successfully.")
    else:
      print("Invalid note number. Please enter a number between 1 and", len(lines))
  except FileNotFoundError:
    print("No notes file found. Please add a note first.")
  except ValueError:
    print("Invalid input. Please enter a valid number.")

while True:
  show_menu()
  choice=input("Enter your choice (1-5): ")
  if choice=="1":
    add_note()
  elif choice=="2":
    view_notes()
  elif choice=="3":
    delete_all_notes()
  elif choice=="4":
    remove_note()
  elif choice=="5":
    print("Thank you for using the Notes Taking App.")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 5.")
