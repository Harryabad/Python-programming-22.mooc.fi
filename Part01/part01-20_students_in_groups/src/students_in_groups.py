# Write your solution here
students = int(input("How many students on the course? "))

size = int(input("Desired group size? "))

groups = students // size
remainder = students % size

if remainder > 0:
    groups += 1


print(f"Number of groups formed: {groups}")