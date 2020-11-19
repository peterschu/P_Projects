




def printBoard(board):
    for i in range(0,9):
        print("|", end = " ")
        for j in range(0,9):
            print(str(board[i][j]) + "|", end = " ")
        print()



def Backtracker(board, row, col):
    #Cheks to see if we have reached the end of the board
    if (row == 8 and col == 9):
        return True
    #checks to see if we have reached the end of the column
    if col == 9:
        row = row + 1
        col = 0
        #checks to see if there is already a number in the next spot,
        #if so move on to the next one

    if board[row][col] > 0:
        return Backtracker(board, row, col+1)
        #places all possible canidates into the board 1-9

    for num in range(1,10):
        #chekcs each canidate before placing it in the board
        if Checker(board, row, col, num):
            board[row][col] = num
            if Backtracker(board, row, col+1):
                return True
        #if no possible canidates remain then we clear the spot and backtrack
        board[row][col] = 0
    return False



def Checker(board, row, col, num):
    #checks the row for duplicate numbers
    for i in range(0,9):
        if board[i][col] == num:
            return False
            #checks the column for duplicate numbers
    for i in range(0,9):
        if board[row][i] == num:
            return False
            #checks box area of the coordinate  [row][col]
    B = row - row%3
    C= col - col%3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i + B][j + C] == num:
                return False

    return True


def main():
    print("bupkiss")
    board =          [ [ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],
                       [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
                       [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
                       [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
                       [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
                       [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
                       [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
                       [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
                       [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ] ]

    if Backtracker(board, 0, 0):
         printBoard(board)

main()
