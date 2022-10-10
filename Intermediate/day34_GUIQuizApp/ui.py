from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 17, "italic")


class QuizInterface:
    # type hint: just can pass Class
    def __init__(self, quiz: QuizBrain):

        self.question = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0/0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250,
                             bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125,
                                                   width=275,
                                                   text="",
                                                   fill=THEME_COLOR,
                                                   font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=right_image,
                                  highlightbackground=THEME_COLOR,
                                  command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image,
                                   highlightbackground=THEME_COLOR,
                                   command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_net_question()

        self.window.mainloop()

    def get_net_question(self):
        self.score_update()
        self.canvas.configure(bg="white")
        if self.question.still_have__questions():
            q_text = self.question.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            end_text = "You have completed all questions.\n\nPlease exit and start a new round."
            self.canvas.itemconfig(self.canvas_text, text=end_text)
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.question.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.question.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_net_question)

    def score_update(self):
        current_score = self.question.score
        current_number = self.question.question_number
        self.score.config(text=f"Score: {current_score}/{current_number}")
