#student garde management
students_score=input("Enter the students score separated bu comma: ")
scores=[int(score) for score in students_score.split(",")]
#step 2: assigning grades using list comprehension
grades=[
    "A" if score>=90 else
    "B" if score>=80 else
    "C" if score>=70 else
    "D" if score>=60 else
    "F" for score in scores
]
#step 3: filter passing and failing students
passing_students=[score for score in scores if score>=60]
failing_students=[score for score in scores if score<60]

#step4:print Results
print("\n-----Student Grade Management-----")
for i,(score,grade) in enumerate(zip(scores,grades),start=1):
  print(f"Student {i}: Score={score}, Grade={grade}")
print("\n---Passing and Failing Student---")
print(f"Passing Students: {passing_students}")
print(f"Failing Students: {failing_students}")


