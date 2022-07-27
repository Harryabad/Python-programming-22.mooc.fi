# Write your solution here

def times_ten(start_index: int, end_index: int):
    my_dictionary = {}
    i = start_index

    while i <= end_index:
        my_dictionary[i] = i*10

        i += 1

    return my_dictionary


if __name__ == "__main__":
    d = times_ten(3,6)
    print(d)