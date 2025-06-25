import csv 

name=input("What's your name? ")
home=input("Where's your home? ")
house=input("What's your house? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home","house"])
    writer.writerow({"name":name, "home":home, "house":house})