# Write your solution here

inp = input("Please type in a string: ")
if len(inp) < 20:
    print("*"*(20-len(inp)) + inp)