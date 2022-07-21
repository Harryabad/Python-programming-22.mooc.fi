# Write your solution here

from operator import contains


def distinct_numbers(my_list):
    newList = []

    for i in my_list:
        if not i in newList:
            newList.append(i)

    

    return sorted(newList)

if __name__ == "__main__":

    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))

