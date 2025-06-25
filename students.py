import csv

students = []

with open("students.csv") as file:

#csv.DictReader is better since it assigns names to the columns 
    reader =csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home":row["home"], "house":row["house"]})
        
#lambda creates an anonymous function that takes a value lambda "X"
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']} in house {student['house']}")