import tkinter as tk
import random
import pyperclip as pc

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
           "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["@", "!", "*", "%", "$"]


# functions


def make_pass():
    pass_box.delete(0, 200)
    password = []
    char_amount = int(char_scale.get())
    for n in range(char_amount):
        password.append(letters[random.randint(0, len(letters) - 1)])

    sym_amount = int(sym_scale.get())
    for n in range(sym_amount):
        password.append(symbols[random.randint(0, len(symbols) - 1)])

    num_amount = int(num_scale.get())
    for n in range(num_amount):
        password.append(numbers[random.randint(0, len(numbers) - 1)])

    random.shuffle(password)
    password_str = ""
    for char in password:
        password_str += char

    pass_box.insert(0, password_str)


def copy_pass():
    pc.copy(pass_box.get())


# main window settings
main_window = tk.Tk()
main_window.configure(background="gainsboro")
main_window.minsize(720, 480)
main_window.title("Zabu's Password Generator (MF)")
main_window.resizable(False, False)

# title area
title = tk.Label(font=("Calibri, Ubuntu", 16), text="Zabu's Password Generator", pady=10, background="gainsboro")
title.pack()

# first seperator
sep1 = tk.Canvas()
sep1.configure(background="gainsboro", width=720, height=0.5, border=0, borderwidth=0, bd=0)
sep1.pack()

# character scale
char_scale_text = tk.Label(font=("Calibri, Ubuntu", 14), text="How many characters do you want in your password?")
char_scale_text.pack()

char_scale = tk.Scale()
char_scale.configure(from_=0, to=32, orient="horizontal", background="gainsboro", bd=0, sliderlength=50,
                     length=300, font=("Calibri, Ubuntu", 16), relief="raised")
char_scale.pack()

# numbers scale
num_scale_text = tk.Label(font=("Calibri, Ubuntu", 14), text="How many numbers do you want in your password?")
num_scale_text.pack()

num_scale = tk.Scale()
num_scale.configure(from_=0, to=32, orient="horizontal", background="gainsboro", bd=0, sliderlength=50,
                    length=300, font=("Calibri, Ubuntu", 16), relief="raised")
num_scale.pack()

# symbols scale
sym_scale_text = tk.Label(font=("Calibri, Ubuntu", 14), text="How many symbols do you want in your password?")
sym_scale_text.pack()

sym_scale = tk.Scale()
sym_scale.configure(from_=0, to=32, orient="horizontal", background="gainsboro", bd=0, sliderlength=50,
                    length=300, font=("Calibri, Ubuntu", 16), relief="raised")
sym_scale.pack()

# "make my pass" button
btn_make_pass = tk.Button(width=20, height=1, text="Make my password", font=("Calibri, Ubuntu", 14), command=make_pass)
btn_make_pass.pack()

# second seperator
sep2 = tk.Canvas()
sep2.configure(background="gainsboro", width=720, height=20, border=0, borderwidth=0, bd=0)
sep2.pack()

# password area
pass_box = tk.Entry()
pass_box.configure(width=40, font=("Calibri, Ubuntu", 20), justify="center", fg="maroon", exportselection=1)
pass_box.insert(0, "Your pass will be here...")
pass_box.pack()

# select and copy the password button
btn_copy = tk.Button(width=20, height=1, text="Copy the password", font=("Calibri, Ubuntu", 14), command=copy_pass)
btn_copy.pack()

main_window.mainloop()
