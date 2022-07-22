# Write your solution here

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

    return newMat
if __name__ == "__main__":

    sudoku = [
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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))

