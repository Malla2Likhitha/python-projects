from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# To continue from the previous progress
try:
    df = pandas.read_csv('./data/words_to_learn.csv')
# if there is no previous progress
except FileNotFoundError:
    df = pandas.read_csv('./data/french_words.csv')
to_learn = df.to_dict(orient='records')
learn_dict = random.choice(to_learn)


def change_and_remove():
    to_learn.remove(learn_dict)
    new_df = pandas.DataFrame(to_learn)
    new_df.to_csv('./data/words_to_learn.csv', index=False)
    change()


def flip():
    global learn_dict
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=learn_dict['English'], fill='white')


def change():
    global learn_dict
    global flip_timer
    if learn_dict != {}:
        learn_dict = random.choice(to_learn)
        # Every card will be shown for 3 sec before flipping,
        # so if we go to a new card before the current card is flipped, the timer will reset.
        window.after_cancel(flip_timer)
        canvas.itemconfig(card, image=front_card)
        canvas.itemconfig(language_text, text='French', fill='black')
        canvas.itemconfig(word_text, text=learn_dict['French'], fill='black')
        flip_timer = window.after(3000, flip)
    else:
        window.after_cancel(flip_timer)
        canvas.itemconfig(card, image=front_card)
        canvas.itemconfig(language_text, text='Congrats!!', fill='black')
        canvas.itemconfig(word_text, text='You have learnt all the words!!', fill='black')


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('Flash Card Game')

flip_timer = window.after(3000, flip, learn_dict)

# Canvas
canvas = Canvas(window, height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file='./images/card_front.png')
back_card = PhotoImage(file='./images/card_back.png')
card = canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))

# Buttons
right_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')
right = Button(image=right_image, highlightthickness=0, bd=0, command=change_and_remove)
right.grid(row=1, column=0)
wrong = Button(image=wrong_image, highlightthickness=0, bd=0, command=change)
wrong.grid(row=1, column=1)

change()

window.mainloop()
