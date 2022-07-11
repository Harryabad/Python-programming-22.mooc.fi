# Write your solution here
inp = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))

count = 1

output = ""
while count <= amount:
    output += inp
    count+=1
print(output)