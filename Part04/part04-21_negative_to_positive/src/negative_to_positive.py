# Write your solution here
number = int(input("Please type in a positive integer: "))

negativeNumber = number *-1

for i in range(negativeNumber, number+1,1):

    if i != 0:
        print(i)