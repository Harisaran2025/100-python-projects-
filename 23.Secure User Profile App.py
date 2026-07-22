#23
class UserProfile:
  def __init__(self,username,email,password):
    self.username=username
    self._email=email
    self.__password=password
    self.set_password(password)

  def get_email(self):
    return self._email

  def set_email(self,new_email):
    if '@' in new_email and "." in new_email:
      self._email=new_email
      print("Email Updated Successfully")
    else:
      print("Invalid email format")

  def set_password(self, new_password):
    if len(new_password) >= 8:
      self.__password = new_password
      print("Password Updated Successfully")
    else:
      print("Password must be at least 8 characters long")

  def display_profile(self):
    print("\n-----User Profile-----")
    print(f"Username: {self.username}")
    print(f"Email: {self._email}")
    print(f"Password: {'*' * len(self.__password)}")

#main program
users =[]
def create_user():
  username = input("Enter username: ").strip()
  email = input("Enter email: ").strip()
  password = input("Enter password: ").strip()
  user = UserProfile(username,email,password)
  users.append(user)
  print("=====User created successfully=====")

def view_profiles():
  if not users:
    print("No users found")
  else:
    print("\n-----User Profiles-----")
    for user in users:
      user.display_profile()

def update_email():
  username= input("Enter username to update profile: ").strip()
  for user in users:
    if user.username ==username:
      new_email = input("Enter new email: ").strip()
      user.set_email(new_email)
      return
  print("User not found")
    

while True:
  print("\n-----User Profile App-----")
  print("1. Create User")
  print("2. View Profiles")
  print("3. Update Email")
  print("4. Exit")
  choice = int(input("Enter your choice (1/2/3/4): ").strip())
  if choice == 1:
    create_user()
  elif choice == 2:
    view_profiles()
  elif choice == 3:
    update_email()
  elif choice == 4:
    print("Exiting User Profile App Thank You")
    break
  else:
    print("Invalid choice please try again")
