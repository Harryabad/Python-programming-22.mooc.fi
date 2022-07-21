# Write your solution here

def most_common_character(string):

    letterCount = {} ## create a dictionary -> if letter not in dictionary will add with count 1. if in dictionary, will increase by 1

    for i in string:
        if i in letterCount:
            letterCount[i] += 1
        else:
            letterCount[i] = 1
    
    #print(letterCount.get(max(letterCount, key = letterCount.get)))

    return max(letterCount, key = letterCount.get)
    

if __name__ == "__main__":
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))