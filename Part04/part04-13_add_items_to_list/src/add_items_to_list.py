# Write your solution here

list = []

totalItems = int(input("How many items: "))

for i in range(1,totalItems+1,1):
    item = int(input(f"Item {i}: "))
    list.append(item)
print(list)