# Ingredients checker
recipe_ing={"flour","sugar","butter","eggs","milk","baking powder"}
user_input=input("Enter the ingredients you have (separated by comma): ")
user_ings=set(user_input.split(","))
print("\n-----Ingredients Checker-----")
missing_ing=recipe_ing - user_ings
extra_ings=user_ings - recipe_ing
print("\n----Ingredients Check Reults----")
if missing_ing:
  print(f"You are missing the following ingredients: {', '.join(missing_ing)}")
else:
  print("You have all the ingredients needed.")
if extra_ings:
  print(f"You have extra ingredients: {', '.join(extra_ings)}")
else:
  print("You Have all the ingredients needed.")
