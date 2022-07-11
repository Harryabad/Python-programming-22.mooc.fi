# Write your solution here

# Write your solution here

inp_year = int(input("Give year:"))
year = inp_year

lyear = year +4

leap = (((year % 400 == 0) and (year % 100 == 0)) or ((year % 4 ==0) and (year % 100 != 0)))

lleap = (((lyear % 400 == 0) and (lyear % 100 == 0)) or ((lyear % 4 ==0) and (lyear % 100 != 0)))


if leap and lleap:
    print(f"The next leap year after {inp_year} is {lyear}")

if leap and not lleap:
    print(f"The next leap year after {inp_year} is {lyear+4}")
while not leap:

    year+=1
    leap = (((year % 400 == 0) and (year % 100 == 0)) or ((year % 4 ==0) and (year % 100 != 0)))

    if leap:
        print(f"The next leap year after {inp_year} is {year}")

    




##      MODEL ANSWER    ##
# start_year = int(input("Year: "))
# year = start_year + 1
# while True:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             break
#     elif year % 4 == 0:
#         break
 
#     year += 1
 
# print(f"The next leap year after {start_year} is {year}")