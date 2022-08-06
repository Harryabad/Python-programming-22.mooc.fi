# Write your solution here

layers = int(input("Layers: "))
size = (layers*2)-1
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
matrix = []
center = size//2

for x in range(size):
    for y in range(size):
        distance_center = max(abs(x-center),abs(y-center))
        letter = letters[distance_center]
        matrix.append(letter)

result = ''
for i in matrix:
    result += i
#print(result)
#unflatten = [matrix[i*size: i*size+size] for i in range(size)]

unflatten = [result[i*size: i*size+size] for i in range(size)]

for row in unflatten:
    print(row)
    
# matrix = [1,2,3,4,5,6,7,8,9]
# size = 3
# unflatten = [result[i*size: i*size+size] for i in range(size)] 
# ^same as
# [result[i*size: i*3+3] for i in range(3)]
# so first iteration where i = 0 will be
# result[0:3] <-> [1,2,3]
# next iteration where i = 1 is
# result[3:6] <-> [4,5,6]
# and lastly where i = 2
# result[6:9] <-> [7,8,9]
# and in the end you have unflatten
# unflatten = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
