# Write your solution here
count, sum, mean, positive, negative = 0,0,0,0,0
print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("PNumber: "))

    if number == 0:
        break
    count += 1
    sum += number

    if (number > 0):
        positive += 1
    else:
        negative += 1

mean = sum / count

print("... the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")
