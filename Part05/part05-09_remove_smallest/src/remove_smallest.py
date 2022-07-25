
def remove_smallest(numbers: list):

    smallestNum = numbers[0]

    for i in numbers:
        if i < smallestNum:
            smallestNum = i

    #print(numbers)
    numbers.remove(smallestNum)

    #print(smallestNum)



if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
