# Write your solution here

def sudoku_grid_correct(sudoku: list):

    
    for i in range(0,9):
        if row_correct(sudoku, i) == False:
            return False

    for i in range(0,9):
        if column_correct(sudoku, i) == False:
            return False

    for row in range(0,9,3):
        for column in range(0,9,3):
            if block_correct(sudoku, row, column) == False:
                return False
    
    
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):

    duplicates = set()
    
    newMat = [sudoku[row_no][column_no:column_no+3],
     sudoku[row_no+1][column_no:column_no+3],
      sudoku[row_no+2][column_no:column_no+3]]

    for row in newMat:
        for cell in row:
            if cell > 0 and cell in duplicates:
                return False ## duplicate = true therefore row is incorrect (FALSE)
            elif cell > 0:
                duplicates.add(cell)
            #print(cell)
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