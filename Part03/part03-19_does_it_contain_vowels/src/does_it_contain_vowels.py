# Write your solution here

inp = input("Please type in a string: ")
vowels = ["a", "e", "o"]


for elem in vowels:
    if elem in inp:
        print(f"{elem} found")
    else:
        print(f"{elem} not found")