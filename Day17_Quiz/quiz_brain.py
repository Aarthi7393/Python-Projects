from data import question_data
from question_model import Question

# TODO: Asking the questions
class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_input, current_question.answer)
        print(f"Your score is {self.score}\n")

# TODO: check if end of the quiz
    def still_has_question(self):
        return self.question_number < len(self.questions_list)


# TODO: check if answer is correct
    def check_answer(self, user_input, correct_answer):
        if user_input ==  correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")


