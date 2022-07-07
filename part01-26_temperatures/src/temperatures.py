# Write your solution here

tempF = int(input("Please type in a temperature (F): "))

celsius = (tempF - 32) * (5/9)

print(f"{tempF} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")