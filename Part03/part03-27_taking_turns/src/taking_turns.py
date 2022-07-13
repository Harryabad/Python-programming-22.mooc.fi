# Write your solution here

num = int(input("Please type in a number: "))

numbers = []

for i in range(1,num+1):
    numbers.append(i)
#print(numbers)
newNewNumbers = []
while len(numbers) > 0:

    if len(numbers) == 1:
        newNewNumbers.append(numbers[0])
        break
    else:
        newNewNumbers.append(numbers[0])
        newNewNumbers.append(numbers[-1])
        numbers = numbers[1:]
        numbers = numbers[:len(numbers)-1]


for i in newNewNumbers:
    print(i)




