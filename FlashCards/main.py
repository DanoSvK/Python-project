from tkinter import *
from random import randint
import pandas
import math
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')


new_list = data.to_dict(orient="records")
print(len(new_list))
updated_list = new_list
words_to_learn = []

rand_int = False


def change_img(rand_int):
    canvas.itemconfig(card_img, image=card_back_img)
    random_en_word = new_list[rand_int]["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_en_word, fill="white")


def next_card():
    global rand_int, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_img, image=card_front_img)
    rand_int = math.floor(randint(0, len(new_list) - 1))
    random_fr_word = new_list[rand_int]["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_fr_word, fill="black")
    flip_timer = window.after(3000, change_img, rand_int)


def is_known():
    if rand_int is not False:
        updated_list.pop(rand_int)
        pandas.DataFrame(updated_list).to_csv("./data/words_to_learn.csv", index=False)
        next_card()


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, change_img, rand_int)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()


