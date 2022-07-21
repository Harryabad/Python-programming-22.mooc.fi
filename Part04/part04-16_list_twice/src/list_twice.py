# Write your solution here
list = []
while True:

    numb = int(input("New item: "))

    if numb == 0:
        print("Bye!")
        break
    list.append(numb)

    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}") ## sorted is a function that returns sorted list
                                                ## list.sort() will sort list in place