# ToDo: asking the question
# ToDo: checking if the answer is correct
# ToDo: checking if we're the end of quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        # default value
        self.question_number = 0
        self.score = 0

    def still_have__questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # remember the self attributes
        current_question = self.question_list[self.question_number]
        ask = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(ask, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The right answer is {correct_answer}")
        print(f"You current score is: {self.score}/{self.question_number}.\n\n")

