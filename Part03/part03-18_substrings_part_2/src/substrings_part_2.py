# Write your solution here
inp = input("Please type in a string: ")

index = len(inp)

while index >= 0:
    print(inp[index: len(inp)])
    index -= 1