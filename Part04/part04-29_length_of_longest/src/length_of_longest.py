# Write your solution here

def length_of_longest(my_list):

    length = 0

    for i in my_list:
        if len(i) > length:
            length = len(i)

    return length

if __name__ == "__main__":

    my_list1 = ["first", "second", "fourth", "eleventh"]
    my_list2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result1 = length_of_longest(my_list1)
    result2 = length_of_longest(my_list2)

    print(result1)
    print(result2)

