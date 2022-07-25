# Write your solution here

def transpose(matrix: list):

    #Below works but bad code

    # matrixT = [ [ 0 for i in range(len(matrix)) ] for j in range(len(matrix)) ]

    # for i in range(len(matrix)):
    #     for j in range(len(matrix)):
    #         matrixT[i][j] = matrix[j][i]

    # for i in range(len(matrix)):
    #     for j in range(len(matrix)):
    #         matrix[i][j] = matrixT[i][j]


    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


    

if __name__ == "__main__":

    m = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    print(m)
    transpose(m)
    print(m)