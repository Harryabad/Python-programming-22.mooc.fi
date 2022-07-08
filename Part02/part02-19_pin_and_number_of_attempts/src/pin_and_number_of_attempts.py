# Write your solution here

pin = 4321
count = 0

while True:
    pInput = int(input("PIN: "))

    if pInput != pin:
        print("Wrong")
        count = count + 1
    elif pInput == pin:
        count = count + 1
        break

if count == 1 :
    print(f"Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {count} attempts")