# ToDo: asking the question
# ToDo: checking if the answer is correct
# ToDo: checking if we're the end of quiz
import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        # default value
        self.question_number = 0
        self.score = 0
        self.current_question = None

    def still_have__questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # remember the self attributes
        self.current_question = self.question_list[self.question_number]
        # Use unescape method to decode HTML entities
        format_question = html.unescape(self.current_question.text)
        text = f"Q.{self.question_number + 1}: {format_question} (True/False)?"
        self.question_number += 1
        return text
        # ask = input(f"Q.{self.question_number + 1}: {format_question} (True/False)?: ")
        # self.check_answer(ask)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            return True
        else:
            print("That's wrong.")
            return False

        print(f"You current score is: {self.score}/{self.question_number}.\n\n")

