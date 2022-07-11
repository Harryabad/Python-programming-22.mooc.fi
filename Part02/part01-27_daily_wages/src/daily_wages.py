# Write your solution here
hourlyWage = float(input("Hourly wage: "))
hoursWorked = int(input("Hours worked: "))
day = input("Day of the week: ")
total = 0
if day == "Sunday":
    total = hourlyWage * hoursWorked *2
else:
    total = hourlyWage * hoursWorked

print(f"Daily wages: {total} euros")