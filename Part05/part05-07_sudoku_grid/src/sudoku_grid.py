# Write your solution here

def sudoku_grid_correct(sudoku: list):

    duplicates1 = set()
    duplicates2 = set()
    duplicates3 = set()
    duplicates4 = set()
    duplicates5 = set()
    duplicates6 = set()
    duplicates7 = set()
    duplicates8 = set()
    duplicates9 = set()

    gridDuplicates = []
    
    newMat1 = [sudoku[0][0:3],
     sudoku[1][0:3],
      sudoku[2][0:3]]

    newMat2 = [sudoku[0][3:6],
     sudoku[1][3:6],
      sudoku[2][3:6]]

    newMat3 = [sudoku[0][6:9],
     sudoku[1][6:9],
      sudoku[2][6:9]]

    newMat4 = [sudoku[3][0:3],
     sudoku[4][0:3],
      sudoku[5][0:3]]

    newMat5 = [sudoku[3][3:6],
     sudoku[4][3:6],
      sudoku[5][3:6]]

    newMat6 = [sudoku[3][6:9],
     sudoku[4][6:9],
      sudoku[5][6:9]]

    newMat7 = [sudoku[6][0:3],
     sudoku[7][0:3],
      sudoku[8][0:3]]

    newMat8 = [sudoku[6][3:6],
     sudoku[7][3:6],
      sudoku[8][3:6]]

    newMat9 = [sudoku[6][6:9],
     sudoku[7][6:9],
      sudoku[8][6:9]]

    #print(newMat6)

    for row in newMat1:
        for cell in row:
            if cell > 0 and cell in duplicates1:
                return False ## duplicate = ture therefore row is incorrect (FALSE)
            elif cell > 0:
                duplicates1.add(cell)
    
    for row in newMat2:
        for cell in row:
            if cell > 0 and cell in duplicates2:
                return False ## duplicate = ture therefore row is incorrect (FALSE)
            elif cell > 0:
                duplicates2.add(cell)
 
    for row in newMat3:
        for cell in row:
            if cell > 0 and cell in duplicates3:
                return False ## duplicate = ture therefore row is incorrect (FALSE)
            elif cell > 0:
                duplicates3.add(cell)

    for row in newMat4:
        for cell in row:
            if cell > 0 and cell in duplicates4:
                return False ## duplicate = ture therefore row is incorrect (FALSE)
            elif cell > 0:
                duplicates4.add(cell) 

    for row in newMat5:
        for cell in row:
            if cell > 0 and cell in duplicates5:
                return False ## duplicate = ture therefore row is incorrect (FALSE)
            elif cell > 0:
                duplicates5.add(cell)

    for row in newMat6:
        for cell in row:
            if cell > 0 and cell in duplicates6:
                return False ## duplicate = ture therefore row is incorrect (FALSE)
            elif cell > 0:
                duplicates6.add(cell)

    for row in newMat7:
        for cell in row:
            if cell > 0 and cell in duplicates7:
                return False ## duplicate = ture therefore row is incorrect (FALSE)
            elif cell > 0:
                duplicates7.add(cell)

    for row in newMat8:
        for cell in row:
            if cell > 0 and cell in duplicates8:
                return False ## duplicate = ture therefore row is incorrect (FALSE)
            elif cell > 0:
                duplicates8.add(cell)

    for row in newMat9:
        for cell in row:
            if cell > 0 and cell in duplicates9:
                return False ## duplicate = ture therefore row is incorrect (FALSE)
            elif cell > 0:
                duplicates9.add(cell)

    
    for i in range(0,8,1):
        if row_correct(sudoku, i) == False:
            return False

    for i in range(0,8,1):
        if column_correct(sudoku, i) == False:
            return False
    
    
    return True

def row_correct(sudoku: list, row_no: int):

    duplicates = set()

    for cell in sudoku[row_no]:
        if cell > 0 and cell in duplicates:
            return False ## duplicate = ture therefore row is incorrect (FALSE)
        elif cell > 0:
            duplicates.add(cell)
            #print(cell)
    return True

def column_correct(sudoku: list, column_no: int):

    duplicates = set()

    for row in sudoku:
        #print(row[column_no])
        if row[column_no] > 0 and row[column_no] in duplicates:

            return False ## duplicate = ture therefore row is incorrect (FALSE)
        elif row[column_no] > 0:
            duplicates.add(row[column_no])
                #print(cell)
    #print(duplicates)
    return True

if __name__ == "__main__":

    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
        ]

    print(sudoku_grid_correct(sudoku2))

    sudoku = [
        [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
        [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
        [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
        [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
        [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
        [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
        [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
        [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
        [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
        ]
    print(sudoku_grid_correct(sudoku))