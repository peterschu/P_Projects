from tkinter import *
from tkinter import messagebox
class Sudoku():
    def __init__(self, board):
        self.counter = 0 #Counts errors
        self.EndCounter = 0 #counts how many more numbers are needed to victory
        self.completeB = board #The completed array
        self.root = Tk()
        self.label = [ [ 0 for i in range(9) ] for j in range(9) ]
        self.array =  [ [ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],    #The default array
                           [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
                           [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
                           [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
                           [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
                           [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
                           [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
                           [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
                           [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ] ]
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
        self.button = Button(self.root,height = 2,width = 10,text="CLEAR",command=self.Clear)

#places in the given numbers and increases the end counter
        for r in range(9):
           for c in range(9):
               self.label[r][c].grid(row=r,column=c)
               if self.array[r][c] > 0:
                   self.label[r][c].insert(INSERT, self.array[r][c])
                   self.label[r][c].config( state=DISABLED)
                   self.EndCounter= self.EndCounter +1

        self.button.grid(row= 10, column = 10)
        self.ErrorBlock.grid(row= 10, column =4)
        self.root.mainloop()

#Clears Game Board and resets counters
    def Clear(self):
        for r in range(9):
           for c in range(9):
               if self.array[r][c] == 0:
                   self.label[r][c].config( state=NORMAL)
                   self.label[r][c].delete(0, "end")
        self.counter = 0
        self.EndCounter = 0
        self.ErrorBlock.config(text =" X's : " + str(self.counter))

#When the Enter Key is Pressed it will do this function to check the answer and increase the wrong counter
    def onReturn(self, row, col):
        if self.label[row][col].get() == str(self.completeB[row][col]): #if the users answer is correct correct place into box
            self.label[row][col].config( state=DISABLED)
            self.EndCounter= self.EndCounter +1
        elif self.label[row][col].get() != "": #if the user's answer is false then clear answer and increase error counter
            self.counter = self.counter+1
            self.ErrorBlock.config(text =" X's : " + str(self.counter))
            self.label[row][col].delete(0, "end")
        if self.EndCounter >= 81: #if the board is filled then display victory message
            messagebox.showinfo("Winner", "You win ya little smarty")






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
        app=Sudoku(board)


main()
