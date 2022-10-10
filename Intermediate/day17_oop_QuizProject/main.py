from question_model import Question
from data import question_data2
from quiz_brain import QuizBrain

# Write a loop to iterate over the question_data
# Create a Question object from each entry in question_data
# Append each Question object to the question_bank
question_bank = []
for question in question_data2:  # Remember this way to loop the list!!!!
    # print(question)
    # question_text = question["text"]
    # question_answer = question["answer"]
    # Benefits of OOP: when change the question_data/question_data2, just change the key
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_have__questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
