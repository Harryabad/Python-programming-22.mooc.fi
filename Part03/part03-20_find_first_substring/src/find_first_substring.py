# Write your solution here

inp = input("Please type in a word: ")
char =  input("Please type in a character: ")

index = inp.find(char)

if index < len(inp)-3:
    print(inp[index: index+3])
        