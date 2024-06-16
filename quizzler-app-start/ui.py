from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
timer = None


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.game = True

        true = PhotoImage(file='./images/true.png')
        false = PhotoImage(file='./images/false.png')

        self.score_label = Label(text=f'Score: 0', bg=THEME_COLOR, fg='white', font=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, height=250, width=300)
        self.q_txt = self.canvas.create_text(150, 125, text='Hi!', font=('Arial', 20, 'italic'), width=270)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=50)

        self.right = Button(image=true, bd=0, highlightthickness=0, command=self.is_true_button)
        self.right.grid(row=2, column=0)
        self.wrong = Button(image=false, bd=0, highlightthickness=0, command=self.is_false_button)
        self.wrong.grid(row=2, column=1)

        self.next_q()

        self.window.mainloop()

    def next_q(self):
        self.canvas.config(bg='white')
        self.right['state'] = 'normal'
        self.wrong['state'] = 'normal'
        q_text = self.quiz_brain.next_question()
        print(q_text)
        self.canvas.itemconfig(self.q_txt, text=q_text)

    def is_true_button(self):
        self.feedback('true')

    def is_false_button(self):
        self.feedback('false')

    def feedback(self, tf):
        self.right['state'] = 'disabled'
        self.wrong['state'] = 'disabled'
        if self.game:
            if self.quiz_brain.check_answer(tf):
                self.canvas.config(bg='green')
            else:
                self.canvas.config(bg='red')
            self.score_label.config(text=f'Score: {self.quiz_brain.score}')
            if self.quiz_brain.still_has_questions():
                self.window.after(1000, self.next_q)
            else:
                self.window.after(1000, self.end)
                self.right['state'] = 'disabled'
                self.wrong['state'] = 'disabled'

    def end(self):
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.q_txt, text="You've completed the quiz\n"
                                                f"Your final score was: "
                                                f"{self.quiz_brain.score}/{self.quiz_brain.question_number}")
        self.game = False
