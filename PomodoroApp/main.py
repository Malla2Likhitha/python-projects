from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas1.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    checks.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:   # Long Break
        title_label.config(text='Long Break', fg=RED)
        countdown(int(LONG_BREAK_MIN * 60))
    elif reps % 2 == 0:   # Short Break
        title_label.config(text='Short Break', fg=PINK)
        countdown(int(SHORT_BREAK_MIN * 60))
    else:   # Work
        title_label.config(text='Work', fg=GREEN)
        countdown(int(WORK_MIN * 60))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(sec):
    global timer
    checkmarks = ''
    count_in_min = sec // 60
    count_in_sec = sec % 60
    if count_in_min < 10:
        count_in_min = f'0{count_in_min}'
    if count_in_sec < 10:
        count_in_sec = f'0{count_in_sec}'
    canvas1.itemconfig(timer_text, text=f'{count_in_min}:{count_in_sec}')
    if sec != 0:
        timer = window.after(1000, countdown, sec - 1)
    else:   # sec == 0
        for i in range(int((reps + 1)/2)):
            checkmarks += '✔'
            checks.config(text=checkmarks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50)
window.config(bg=YELLOW)

# Create Label
title_label = Label(text='Timer', font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)
checks = Label(text='', font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
checks.grid(row=3, column=1)

# Create Canvas
canvas1 = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
bg = PhotoImage(file="tomato.png")
canvas1.create_image(100, 112, image=bg)
timer_text = canvas1.create_text(100, 130, text='00:00', font=(FONT_NAME, 30, 'bold'), fill='white')
canvas1.grid(row=1, column=1)

# Create Buttons
start = Button(text='Start', command=start_timer)
start.grid(row=2, column=0)
reset = Button(text='Reset', command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()
