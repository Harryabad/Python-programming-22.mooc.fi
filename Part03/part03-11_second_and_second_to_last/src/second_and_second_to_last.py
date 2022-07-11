# Write your solution here

inp = input("Please type in a string: ")

secondChar = inp[1]
secondtoLastChar = inp[len(inp)-2]

if secondChar == secondtoLastChar:
    print(f"The second and the second to last characters are {secondChar}")
else:
    print("The second and the second to last characters are different")

