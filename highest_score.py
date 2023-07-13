# List of students with their names and scores
students = [("Alice", 85), ("Bob", 92), ("Charlie", 88), ("David", 95), ("Eve", 90)]

# Finding the student with the highest score
highest_score = 0
top_student = ""

for  name, score in students:
    if score > highest_score:
        highest_score = score
        top_student = name

# Displaying the student with the highest score
print("Student with the highest score:")
print("Name:", top_student)
print("Score:", highest_score)
