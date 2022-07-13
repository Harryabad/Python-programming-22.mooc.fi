# Write your solution here

num = int(input("Please type in a number: "))

for i in range(num):
    i = i+1
    for j in range(num):
        j = j+1
        print(f"{i} x {j} = {i*j}")

        