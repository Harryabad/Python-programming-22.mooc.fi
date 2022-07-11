# Write your solution here

limit = int(input("Limit: "))

value = 1
sum = 1

consecutive = "1"
while sum < limit:

    value += 1
    sum += value
    

    consecutive += (f" + {value}")
   
    

print(f"The consecutive sum: {consecutive} = {sum}")
