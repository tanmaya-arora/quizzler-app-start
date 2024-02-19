from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.qb = quiz_brain
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="#ffffff")
        self.score_label.grid(column=2, row=1)

        self.empty_label = Label(text="", bg=THEME_COLOR)
        self.empty_label.grid(column=1, row=2)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125, text="", width=280, fill=THEME_COLOR, font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=1, row=3, columnspan=2)

        self.empty_label2 = Label(text="", bg=THEME_COLOR)
        self.empty_label2.grid(column=1, row=4)

        self.right_img = PhotoImage(file="./images/true.png")
        self.wrong_img = PhotoImage(file="./images/false.png")

        self.right_btn = Button(
            image=self.right_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.right_btn.grid(column=1, row=5)

        self.wrong_btn = Button(
            image=self.wrong_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.wrong_btn.grid(column=2, row=5)

        self.canvas.itemconfig(self.question_text, text=quiz_brain.next_question())

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=self.qb.next_question())

    def true_pressed(self):
        answer = self.qb.check_answer("true")
        self.score = answer['score']
        self.score_label.destroy()
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="#ffffff")
        self.score_label.grid(column=2, row=1)

        if answer['answer']:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.update()

        if self.qb.still_has_questions():
            self.window.after(1000, self.get_next_question())
            # self.canvas.itemconfig(self.question_text, text=self.qb.next_question())
        else:
            self.score_label.destroy()
            self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="#ffffff")
            self.score_label.grid(column=2, row=1)
            time.sleep(3)
            self.window.destroy()

    def false_pressed(self):
        answer = self.qb.check_answer("false")
        self.score = answer['score']
        self.score_label.destroy()
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="#ffffff")
        self.score_label.grid(column=2, row=1)

        if answer['answer']:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.update()

        if self.qb.still_has_questions():
            self.window.after(1000, self.get_next_question())
            # self.canvas.itemconfig(self.question_text, text=self.qb.next_question())
        else:
            self.score_label.destroy()
            self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="#ffffff")
            self.score_label.grid(column=2, row=1)
            time.sleep(3)
            self.window.destroy()
