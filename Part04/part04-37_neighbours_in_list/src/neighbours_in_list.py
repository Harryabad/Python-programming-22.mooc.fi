# Write your solution heres

def longest_series_of_neighbours(my_list):

    count = 0
    listCount = []
    maxCount = 0
        
    pairs = [[my_list[i], my_list[i + 1]] for i in range(len(my_list) - 1)]
    print(pairs)

    pairs = [abs(pairs[i][0] - pairs[i][1]) for i in range(len(pairs))]
    print(pairs)


    for i in pairs:
        if i == 1:
            count += 1
        else:
            listCount.append(count)
            count = 0
    listCount.append(count)
    print(listCount)

    maxCount = max(listCount)

    
    return maxCount + 1
    


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))