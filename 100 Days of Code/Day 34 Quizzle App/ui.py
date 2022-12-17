from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class UserInterface():

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question", width=280, fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.correct_button = Button()
        self.img_correct_button = PhotoImage(
            file=r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 34 Quizzle App\images\true.png")
        self.correct_button.config(
            image=self.img_correct_button, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(row=2, column=0)
        self.wrong_button = Button()
        self.img_wrong_button = PhotoImage(
            file=r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 34 Quizzle App\images\false.png")
        self.wrong_button.config(
            image=self.img_wrong_button, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
