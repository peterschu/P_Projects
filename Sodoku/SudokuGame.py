from tkinter import *
from tkinter import messagebox

def printBoard(board):
    for i in range(0,9):
        print("|", end = " ")
        for j in range(0,9):
            print(str(board[i][j]) + "|", end = " ")
        print()



def Backtracker(board, row, col):
    #Checks to see if we have reached the end of the board
    if (row == 8 and col == 9):
        return True
    #Checks to see if we have reached the end of the column
    if col == 9:
        row = row + 1
        col = 0
        #Checks to see if there is already a number in the next spot,
        #If so move on to the next one

    if board[row][col] > 0:
        return Backtracker(board, row, col+1)
        #Places all possible canidates into the board 1-9

    for num in range(1,10):
        #Checks each candidate before placing it in the board
        if Checker(board, row, col, num):
            board[row][col] = num
            if Backtracker(board, row, col+1):
                return True
        #If no possible candidates remain then we clear the spot and backtrack
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


class Sudoku():
    def __init__(self):
        self.BN = 1
        self.counter = 0 #Counts errors
        self.EndCounter = 0 #counts how many more numbers are needed to victory
        self.root = Tk()
        self.label = [ [ 0 for i in range(9) ] for j in range(9) ]

        self.array = [[[ 0 for i in range(2) ]  for k in range(9) ] for j in range(9)]
        self.array[0] =     [ [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],    #The default array
                           [ 6, 0, 0, 1, 9 ,5 ,0, 0, 0 ],
                           [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                           [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                           [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
                           [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                           [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                           [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
                           [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ] ]

        self.array[1]  =[      [7, 8, 0, 4, 0, 0, 1, 2, 0],
                            [6, 0, 0, 0, 7, 5, 0, 0, 9],
                            [0, 0, 0, 6, 0, 1, 0, 7, 8],
                            [0, 0, 7, 0, 4, 0, 2, 6, 0],
                            [0, 0, 1, 0, 5, 0, 9, 3, 0],
                            [9, 0, 4, 0, 6, 0, 0, 0, 5],
                            [0, 7, 0, 3, 0, 0, 0, 1, 2],
                            [1, 2, 0, 0, 0, 7, 4, 0, 0],
                            [0, 4, 9, 2, 0, 6, 0, 0, 7]]



        self.Solved = [[[ 0 for i in range(2) ]  for k in range(9) ] for j in range(9)]
        self.Solved[0] =     [ [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],    #The default array
                           [ 6, 0, 0, 1, 9 ,5 ,0, 0, 0 ],
                           [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                           [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                           [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
                           [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                           [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                           [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
                           [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ] ]

        self.Solved[1]  =[      [7, 8, 0, 4, 0, 0, 1, 2, 0],
                            [6, 0, 0, 0, 7, 5, 0, 0, 9],
                            [0, 0, 0, 6, 0, 1, 0, 7, 8],
                            [0, 0, 7, 0, 4, 0, 2, 6, 0],
                            [0, 0, 1, 0, 5, 0, 9, 3, 0],
                            [9, 0, 4, 0, 6, 0, 0, 0, 5],
                            [0, 7, 0, 3, 0, 0, 0, 1, 2],
                            [1, 2, 0, 0, 0, 7, 4, 0, 0],
                            [0, 4, 9, 2, 0, 6, 0, 0, 7]]
        Backtracker(self.Solved[0], 0, 0)
        Backtracker(self.Solved[1], 0, 0)

        self.ErrorBlock = Label(self.root,
        height = 2,
        width = 5,
        fg = "red",
        text = " X's : " + str(self.counter),
        font=("Calibri",20))

        for r in range(9): #makes each Label[r][c] an Entry widget
           for c in range(9):
              self.label[r][c] = Entry(self.root,font=("Calibri",50),width = 3,)
              self.label[r][c].bind("<Return>", lambda event, R=r, C=c,: self.onReturn(R, C)) #binds label to enter key


#button to clear board
        self.button = Button(self.root,height = 2,width = 10,text="Change Board",command=self.Clear)

#places in the given numbers and increases the end counter
        for r in range(9):
           for c in range(9):
               self.label[r][c].grid(row=r,column=c)
               if self.array[self.BN][r][c] > 0:
                   self.label[r][c].insert(INSERT, self.array[self.BN][r][c])
                   self.label[r][c].config( state=DISABLED)
                   self.EndCounter= self.EndCounter +1

        self.button.grid(row= 10, column = 10)
        self.ErrorBlock.grid(row= 10, column =4)
        self.root.mainloop()

#Clears Game Board and resets counters
    def Clear(self):
        if self.BN == 0:
            self.BN = self.BN + 1
        else:
            self.BN = 0

        for r in range(9):
           for c in range(9):
                   self.label[r][c].config( state=NORMAL)
                   self.label[r][c].delete(0, "end")
        for r in range(9):
           for c in range(9):
               self.label[r][c].grid(row=r,column=c)
               if self.array[self.BN][r][c] > 0:
                   self.label[r][c].insert(INSERT, self.array[self.BN][r][c])
                   self.label[r][c].config( state=DISABLED)
                   self.EndCounter= self.EndCounter +1

        self.counter = 0
        self.EndCounter = 0
        self.ErrorBlock.config(text =" X's : " + str(self.counter))

#When the Enter Key is Pressed it will do this function to check the answer and increase the wrong counter
    def onReturn(self, row, col):
        if self.label[row][col].get() == str(self.Solved[self.BN][row][col]): #if the users answer is correct correct place into box
            self.label[row][col].config( state=DISABLED)
            self.EndCounter= self.EndCounter +1
        elif self.label[row][col].get() != "": #if the user's answer is false then clear answer and increase error counter
            self.counter = self.counter+1
            self.ErrorBlock.config(text =" X's : " + str(self.counter))
            self.label[row][col].delete(0, "end")
        if self.EndCounter >= 81: #if the board is filled then display victory message
            messagebox.showinfo("Winner", "You win ya little smarty")


app=Sudoku()
