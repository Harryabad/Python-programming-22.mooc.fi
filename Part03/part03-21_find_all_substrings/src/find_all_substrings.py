# Write your solution here

inp = input("Please type in a word: ")
char =  input("Please type in a character: ")

index = inp.find(char)


list = [i for i in range(len(inp)) if inp.startswith(char, i)]


for i in list:
    if i <= len(inp)-3:
        print(inp[i: i+3])


    

        