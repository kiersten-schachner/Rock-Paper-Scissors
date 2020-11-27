from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, ttk, StringVar, PhotoImage, Image, Toplevel
from random import *

class RockPaperScissors:

    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors!")

        self.total = 0
        self.user_move = ""
        self.comp_move = ""
        self.user_wins = 0
        self.comp_wins = 0

        self.label = Label(master, bg = 'lightblue', text="Whoever gets to two wins first wins!", font=('Helvetica', 18, 'bold'))
        self.title = Label(master, bg = 'lightblue', text="Pick one of the following:", font=('Helvetica', 14, 'bold'))
        self.user_label = Label(master, bg = 'lightblue', text="You chose:", font=('Helvetica', 14, 'bold'))
        self.user_chose = StringVar()
        self.user_chose_label = Label(master, bg = 'lightblue', textvariable=self.user_chose, font=('Helvetica', 14))
        self.comp_label = Label(master, bg = 'lightblue', text="Computer chose:", font=('Helvetica', 14, 'bold'))
        self.comp_chose = StringVar()
        self.comp_chose_label = Label(master, bg = 'lightblue', textvariable=self.comp_chose, font=('Helvetica', 14))
        self.winner_label = Label(master, bg = 'lightblue', text="Winner:", font=('Helvetica', 14, 'bold'))
        self.winner = StringVar()
        self.the_winner = Label(master, bg = 'lightblue', textvariable=self.winner, font=('Helvetica', 14))
        self.game_over = StringVar()
        self.game_over_label = Label(master, bg = 'lightblue', textvariable=self.game_over, font=('Helvetica', 14, 'bold'))
        self.game_winner = StringVar()
        self.overall_winner = Label(master, bg = 'lightblue', textvariable=self.game_winner, font=('Helvetica', 14))

        self.rock = ttk.Button(master, text='Rock',  command=lambda: self.choose("Rock"))
        self.paper = ttk.Button(master, text="Paper", command=lambda: self.choose("Paper"))
        self.scissors = ttk.Button(master, text="Scissors", command=lambda: self.choose("Scissors"))

        # LAYOUT
        self.label.pack()
        self.title.pack()
        self.rock.pack()
        self.paper.pack()
        self.scissors.pack()
        self.user_label.pack()
        self.user_chose_label.pack()
        self.comp_label.pack()
        self.comp_chose_label.pack()
        self.winner_label.pack()
        self.the_winner.pack()
        self.game_over_label.pack()
        self.overall_winner.pack()

    def comp_play(self):
        c = randint(0,2)
        options = ['Rock', 'Paper', 'Scissors']
        self.comp_move = options[c]
        self.comp_chose.set(self.comp_move)

    def choose(self, method):
        self.game_over.set("")
        self.game_winner.set("")
        if method == "Rock":
            self.user_move = "Rock"
            self.user_chose.set(self.user_move)
            self.comp_play()
            self.find_winner(self.comp_move, self.user_move)

        elif method == "Paper":
            self.user_move = "Paper"
            self.user_chose.set(self.user_move)
            self.comp_play()
            self.find_winner(self.comp_move, self.user_move)
            
        elif method == "Scissors":
            self.user_move = "Scissors"
            self.user_chose.set(self.user_move)
            self.comp_play()
            self.find_winner(self.comp_move, self.user_move)

    def find_winner(self, comp, user):
        o = ['You!', 'Computer!']
        win = ''
        print(comp)
        print(user)
        if user == comp:
            self.winner.set("Tie!")
        elif user == "Rock":
            if comp == "Scissors":
                self.winner.set(o[0])
                win = o[0]
            else:
                self.winner.set(o[1])
                win = o[1]
                
        elif user == "Paper":
            if comp == "Rock":
                self.winner.set(o[0])
                win = o[0]
            else:
                self.winner.set(o[1])
                win = o[1]
        elif user == "Scissors":
            if comp == "Paper":
                self.winner.set(o[0])
                win = o[0]
            else:
                self.winner.set(o[1])
                win = o[1]

        if win == o[0]:
            self.user_wins += 1
        elif win == o[1]:
            self.comp_wins += 1

        if self.user_wins >= 2:
            self.game_over.set("Game over!")
            self.game_winner.set("You won the game! You had " + str(self.user_wins) + " wins and the computer had " + str(self.comp_wins) + " wins!")
            self.user_wins = 0
            self.comp_wins = 0
        elif self.comp_wins >= 2:
            self.game_over.set("Game over!")
            self.game_winner.set("Computer won the game! Computer had " + str(self.comp_wins) + " wins and you had " + str(self.user_wins) + " wins!")
            self.user_wins = 0
            self.comp_wins = 0
           

root = Tk()
my_gui = RockPaperScissors(root)
root.configure(bg = 'lightblue')
root.mainloop()