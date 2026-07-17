#library management system
class Book:
  def __init__(self,title,author,isbn):
    self.title=title
    self.author=author
    self.isbn=isbn
    self.is_available=True

  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print(f"ISBN: {self.isbn}")
    print(f"Availability: {'Available' if self.is_available else 'Not Available'}")

class library:
  def __init__(self):
    self.books=[]

  def add_book(self,title,author):
    isbn=len(self.books)+1
    new_book=Book(title,author,isbn)
    self.books.append(new_book)
    print(f"Book '{title}' by {author} added to the library")

#View books
  def display_books(self):
    if not self.books:
      print("No books in the library")
    else:
      print("\n---Library Books Catalog---")
      for book in self.books:
        book.display_info()
        print("-------------------------") 

  def borrow_book(self,isbn):
    for book in self.books:
      if book.isbn==isbn:
        if book.is_available:
          book.is_available=False
          print(f"Book '{book.title}' borrowed successfully")
          return
        else:
          print(f"Book '{book.title}' is not available for borrowing")
          return
    print("Book not found in the library")

  def return_book(self,isbn):
    for book in self.books:
      if book.isbn==isbn:
        if not book.is_available:
          book.is_available=True
          print(f"Book '{book.title}' returned successfully")
          return
        else:
          print(f"Book '{book.title}' is already available in the library")
          return
    print("Book not found in the library")

Library=library()
while True:
    print("\n---Library Management System---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    choice=input("Enter your choice(1/2/3/4/5): ")
    if choice=='1':
      title=input("Enter the book title: ").strip()
      author=input("Enter the author name: ").strip()
      Library.add_book(title,author)
    elif choice=='2':
      Library.display_books()
    elif choice=='3':
      try:
        isbn=int(input("Enter the ISBN of the book to borrow: "))
        Library.borrow_book(isbn)
      except ValueError:
        print("Invalid ISBN. Please enter a number.")
    elif choice=='4':
      try:
        isbn=int(input("Enter the ISBN of the book to return: "))
        Library.return_book(isbn)
      except ValueError:
        print("Invalid ISBN. Please enter a number.")
    elif choice=='5':
      print("Thankyou for using!")
      break
    else:
      print("Invalid choice. Please try again")
