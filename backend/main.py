from schemes import schemes
from matching import find_matches

name = input("Enter your name: ")
age = int(input("Enter your age: "))
income = int(input("Enter annual income: "))
education = input("Enter education: ")

print("\nEligible Schemes:")

found = False

for scheme in schemes:
    if (scheme["min_age"] <= age and
        income <= scheme["max_income"] and
        (scheme["education"] == education or
         scheme["education"] == "Any")):

        print("-", scheme["name"])
        found = True

if not found:
    print("No eligible scheme found.")