#recipe viewer app
def load_recipe(file_path):
  try:
    with open(file_path,'r') as file:
      content=file.read()
      recipes=content.split('\n\n')
      recipe_dict={}
      for recipe in recipes:
        lines=recipe.strip().split('\n')
        if len(lines)>=3:
          name=lines[0]
          ingredients=lines[1].replace("Ingredients:","").strip()
          instruction=lines[2].replace("Instruction:","").strip()
          recipe_dict[name]={'ingredients':ingredients,'instruction':instruction}
      return recipe_dict
  except FileNotFoundError:
    print("File not found")
    return {}
def show_menu():
  print("\n----Recipe Menu:----")
  print("1. View Recipe")
  print("2. List all recipe")
  print("3. Exit")

def view_recipe(recipe_dict):
  name=input("Enter the recipe name: ").strip()
  if name in recipe_dict:
    print(f"\n---Recipe Name: {name} Details---")
    print(f"Ingredients:",recipe_dict[name]['ingredients'])
    print(f"Instruction:",recipe_dict[name]['instruction'])
  else:
    print("Recipe not found")


recipe_file='recipes.txt'
recipes=load_recipe(recipe_file)
while True:
  show_menu()
  choice=input("Enter your choice(1/2/3): ")
  if choice=='1':
    view_recipe(recipes)
  elif choice=='2':
    print("\n---All Recipe---")
    for name in recipes:
      print(name)
  elif choice=='3':
    print("Thankyou for using!")
    break
  else:
    print("Invalid choice Please try again")
