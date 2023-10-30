from tkinter import *
import random



window = Tk()

window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

label = Label(text= player + " turn", font=("consolas", 40 ))
label.pack(side="top")

reset_button = Button(text = "restart", font=("consolas", 20))
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame, text="", font=("consolas"), width=12, height=6)
        board[row][column].grid(row = row, column = column)
window.mainloop()

