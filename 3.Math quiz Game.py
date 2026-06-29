import random
def questions():
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  operator = random.choice(['+', '-', '*'])
  
  if operator == '+':
    answer = num1 + num2
  elif operator == '-':
    answer = num1 - num2
  elif operator == '*':
    answer = num1 * num2
  
  return f"{num1} {operator} {num2}", answer
def math_quiz():
  print("-----Math Quiz-----")
  score = 0
  rounds = 5
  print("\n---Welcome to the Math Quiz Game---\n")
  print("\nYou will be presented with math problems, and you need to provide the correct answers.")
  print("\nLet's begin!")
  
  for i in range(rounds):
    question_str, correct_answer = questions()
    print(f"\nQuestion {i+1}: {question_str}")
    
    try:
      user_answer = int(input("Your answer: "))
      if user_answer == correct_answer:
        print("Correct!")
        score += 1
      else:
        print(f"Wrong! The correct answer is {correct_answer}")
    except ValueError:
      print("Invalid input. Please enter a number.")
      
  print(f"\nQuiz completed! Your score is {score}/{rounds}")
  
  if score == rounds:
    print("Congratulations! You answered all the questions correctly.")
  elif score >= (rounds // 2):
    print("Good job! You did well.")
  else:
    print("Better luck next time!")

math_quiz()
