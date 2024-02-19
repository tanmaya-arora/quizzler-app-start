from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="#ffffff")
        self.score_label.grid(column=2, row=1)

        self.empty_label = Label(text="", bg=THEME_COLOR)
        self.empty_label.grid(column=1, row=2)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=1, row=3, columnspan=2)

        self.empty_label2 = Label(text="", bg=THEME_COLOR)
        self.empty_label2.grid(column=1, row=4)

        self.right_img = PhotoImage(file="./images/true.png")
        self.wrong_img = PhotoImage(file="./images/false.png")

        self.right_btn = Button(image=self.right_img, bg=THEME_COLOR, highlightthickness=0)
        self.right_btn.grid(column=1, row=5)

        self.wrong_btn = Button(image=self.wrong_img, bg=THEME_COLOR, highlightthickness=0)
        self.wrong_btn.grid(column=2, row=5)

        self.window.mainloop()
