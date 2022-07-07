# Write your solution here
print("What is the weather forecast for tomorrow? ")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
clothes1 = "Wear jeans and a T-shirt"
clothes2 = "I recommend a jumper as well"
clothes3 = "Take a jacket with you"
clothes4 = "Make it a warm coat, actually"
clothes5 = "I think gloves are in order"

if temperature > 20:
    print(clothes1)
elif temperature <= 20 and  temperature >10:
    print(clothes1 + "\n" + clothes2)
elif temperature <=10 and temperature > 5:
    print(clothes1 + "\n" + clothes2 + "\n" + clothes3)
elif temperature <=5:
    print(clothes1 + "\n" + clothes2 + "\n" + clothes3 + "\n" + clothes4 + "\n" + clothes5)

if rain == "yes":
    print("Don't forget your umbrella!")
