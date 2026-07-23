class Product:
  total_items = 0 # Initialize total_items as a class variable

  def __init__(self,product_name,price,quantity):
    self.product_name=product_name
    self.price=price
    self.quantity=quantity
    Product.total_items += quantity # Use Product.total_items
#Instance method to show the product details
  def show_product_details(self):
    print("\n-----Product Details-----")
    print(f"Product Name: {self.product_name}")
    print(f"Price: {self.price}")
    print(f"Quantity: {self.quantity}")
    print("------------------------")
#Instance method to sell product
  def sell_product(self,amount):
    if amount <= self.quantity:
      self.quantity -= amount
      Product.total_items -= amount # Use Product.total_items
      print(f"{amount} {self.product_name}(s) sold successfully")
    else:
      print("Insufficient quantity")
#ststic method to calculate discount
  @staticmethod
  def calculate_discount(price,discount_percentage):
    return price *(1 - discount_percentage / 100)

#class method to see total item report
  @classmethod
  def show_total_items(cls):
    print("\n-----Total Items Report-----")
    print(f"\nTotal Items: {cls.total_items}")
    print("------------------------")

#main progarm
products = []

#add product in inventry

def add_product():
  product_name = input("Enter product name: ").strip()
  price = float(input("Enter price: ").strip())
  quantity = int(input("Enter quantity: ").strip())
  product = Product(product_name,price,quantity) # Instantiate Product class
  products.append(product)
  print(f"{quantity} {product_name}(s) Product added successfully")
#display all products
def display_products():
  print("\n-----Inventory-----")
  if not products:
    print("No products found")
  else:
    for product in products:
      product.show_product_details()

#sell product
def sell_product():
  product_name = input("Enter product name: ").strip()
  for product in products:
    if product.product_name == product_name:
      amount = int(input("Enter amount of product to sell: ").strip())
      product.sell_product(amount)
      return # Add return to exit after finding and selling the product
  print("Product not found in inventory") # This should only print if the product is not found
#calculate discount
def discount_price():
  price=float(input("Enter price: ").strip())
  discount_percentage = float(input("Enter discount percentage: ").strip())
  discounted_price = Product.calculate_discount(price,discount_percentage) # Use Product.calculate_discount
  print(f"Discounted price: {discounted_price}")


#main menu
while True:
  print("\n-----Inventory Management System-----")
  print("1. Add Product")
  print("2. Display Products")
  print("3. Sell Product")
  print("4. Calculate Discount")
  print("5. Show Total Items in stock")
  print("6. Exit")
  choice = int(input("Enter your choice (1/2/3/4/5/6): ").strip())
  if choice == 1:
    add_product()
  elif choice == 2:
    display_products()
  elif choice == 3:
    sell_product()
  elif choice == 4:
    discount_price()
  elif choice == 5:
    Product.show_total_items()
  elif choice == 6:
    print("Exiting Inventory Management System")
    break
  else:
    print("Invalid choice")
