# Nested dictionary of 10 students
data = {
    "student1": {"name": "Alice", "marks": [80, 90, 85]},
    "student2": {"name": "Bob", "marks": [70, 60, 75]},
    "student3": {"name": "Charlie", "marks": [95, 100, 90]},
    "student4": {"name": "David", "marks": [88, 76, 92]},
    "student5": {"name": "Eva", "marks": [65, 70, 60]},
    "student6": {"name": "Frank", "marks": [78, 85, 80]},
    "student7": {"name": "Grace", "marks": [90, 92, 89]},
    "student8": {"name": "Hannah", "marks": [55, 60, 58]},
    "student9": {"name": "Ishan", "marks": [82, 79, 88]},
    "student10": {"name": "Rahul", "marks": [95, 60, 65]}
}

highest_avg = 0
top_student = ""

# Loop through dictionary
for student in data:
    marks = data[student]["marks"]
    average = sum(marks) / len(marks)

    if average > highest_avg:
        highest_avg = average
        top_student = data[student]["name"]

print("Student with highest average marks:", top_student)
print("Highest Average:", highest_avg)
