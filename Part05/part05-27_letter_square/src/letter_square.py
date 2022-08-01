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