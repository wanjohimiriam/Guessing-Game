from tkinter import *
import random

attempt = 10
answer= random.randint(1, 99)

def Check_Answer():
    global  attempt
    global text

    attempt -= 1

    guess=int(entry_window.get())

    if answer== guess:
        text.set("You win! Congrats")
        btn_check.place_forget()

    elif attempt == 0:
        text.set("You are out of Attempts")
        btn_check.place_forget()

    elif guess < answer:
        text.set("Incorrect ! You have"+ str(attempt) + "attempts remaining - Go higher!!")

    elif guess > answer:
        text.set("Incorrect ! You have" + str(attempt) + "attempts remaining - Go Lower!!")
        


root = Tk()

root.title("Guess Number")

root.geometry("500x500")

label=Label(root,bd=0, text="Guess the number between 1 & 99")
label.place(x=100, y=50)

entry_window=Entry(root,bd=0,relief=SUNKEN, width= 40, borderwidth=4)
entry_window.place(x=100, y=100)

btn_check = Button(root, text="Check", command=Check_Answer)
btn_check.place(x=100, y=150)

btn_quit = Button(root, text="Quit", command=root.destroy)
btn_quit.place(x=100, y=200)

text= StringVar()
text.set("You have 10 attempts remaining! Good luck!")

guess_attempts= Label(root, textvariable=text)
guess_attempts.place(x=100, y=250)

root.mainloop()