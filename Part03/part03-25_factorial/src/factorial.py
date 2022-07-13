# Write your solution here


while True:
    sum = 1
    num = int(input("Please type in a number: "))

    if num <= 0:
        print("Thanks and bye!")
        break
    
    for i in range(1,num+1):
        sum = sum * i
    print(f"The factorial of the number {num} is {sum}")

    
    
