import csv 

name=input("What's your name? ")
home=input("Where's your home? ")
house=input("What's your house? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home,house])