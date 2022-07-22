# Write your solution here



from turtle import goto


five, four, three, two, one, zero, count, sum, passed = 0,0,0,0,0,0,0,0,0

while True:
    
    userInput = input("Exam points and exercises completed: ")

    if userInput == "":
        break

    eP, eC = userInput.split()
    eP = int(eP)
    eC = int(eC)

    eC = eC//10

    score = eP + eC

    sum += score
    count += 1



    if score < 15:
        zero += 1
    elif (score >= 15 and score <= 17):
        if eP >= 10:
            one +=1
        else:
            zero += 1
    elif score >= 18 and score <=20:
        if eP >= 10:
            two +=1
        else:
            zero += 1
    elif score >= 18 and score <=23:
        if eP >= 10:
            three +=1
        else:
            zero += 1
    elif score >= 24 and score <=27:
        if eP >= 10:
            four +=1
        else:
            zero += 1
    elif score >= 28 and score <=30:
        if eP >= 10:
            five +=1
        else:
            zero += 1



print("Statistics:")
print(f"Points average: {sum/count:.1f}")
print(f"Pass percentage: {(five+four+three+two+one)/count * 100:.1f}")
print("Grade distribution:")

print(f"5: {'*'*five}")
print(f"4: {'*'*four}")
print(f"3: {'*'*three}")
print(f"2: {'*'*two}")
print(f"1: {'*'*one}")
print(f"0: {'*'*zero}")

   


