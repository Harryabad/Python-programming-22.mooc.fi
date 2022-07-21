# Write your solution here

def everything_reversed(my_list):

    newList = []

    for i in my_list:
        i = i[::-1]
        newList.append(i)

    newList = newList[::-1]
    return newList


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)