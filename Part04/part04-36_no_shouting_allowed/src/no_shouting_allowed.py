# Write your solution here

def no_shouting(my_list):

    newList = []

    for i in my_list:
        if not i.isupper():
            newList.append(i)
    
    return newList


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)