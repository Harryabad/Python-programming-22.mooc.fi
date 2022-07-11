# Write your solution here

inp = input("Word: ")
print("*"*30)
if len(inp) % 2 == 0:
    print("*" + " "*(14-(len(inp)//2))+ inp + " "*(14-(len(inp)//2)) + "*")
else:
    print("*" + " "*(14-(len(inp)//2)-1)+ inp + " "*(14-(len(inp)//2)) + "*")
print("*"*30)