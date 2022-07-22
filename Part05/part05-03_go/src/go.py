# Write your solution here

def who_won(game_board: list):

    empty, player1, player2 = 0,0,0

    for row in game_board:
        for cell in row:
            if cell == 0:
                empty += 1
            if cell == 1:
                player1 += 1
            if cell == 2:
                player2 +=1
    if player1 > player2:
        return 1
    if player2 > player1:
        return 2
    if player1 == player2:
        return 0


if __name__ == "__main__":
    go = [[1, 2, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]
    print(who_won(go))