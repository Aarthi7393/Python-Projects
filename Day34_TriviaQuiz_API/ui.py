from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_label = Label(bg=THEME_COLOR, text = "Score: 0", fg= "white")

        self.canvas = Canvas(bg = "white", width = 300, height = 250)
        self.q_text = self.canvas.create_text(150,125,text="Question: ",font=("Arial", 15, "italic"), fill=THEME_COLOR
                                              , width = 280)

        right_button = PhotoImage(file="./images/true.png")
        wrong_button = PhotoImage(file="./images/false.png")
        self.rbutton = Button(image= right_button, highlightthickness=0, command= self.right_button, bd= 0)
        self.wbutton = Button(image= wrong_button, highlightthickness=0, command= self.wrong_button, bd= 0)

        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.rbutton.grid(row=2, column=0)
        self.wbutton.grid(row=2, column=1)


        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
            self.rbutton.config(state = "normal")
            self.wbutton.config(state = "normal")
        else:
            self.canvas.itemconfig(self.q_text, text="You have reached the end of the quiz")
        self.canvas.config(bg="white")


    def right_button(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def wrong_button (self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self,is_right ):
        self.rbutton.config(state="disabled")
        self.wbutton.config(state="disabled")
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg= "red")
        self.window.after(1000, self.get_next_question)