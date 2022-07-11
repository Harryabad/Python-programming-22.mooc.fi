# Write your solution here

limit = int(input("Limit: "))

value = 0
sum = 0
while sum < limit:
    sum += value
    value += 1

print(sum)
