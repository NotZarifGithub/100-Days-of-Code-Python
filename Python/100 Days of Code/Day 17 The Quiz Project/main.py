from question_model import Question
from data import question_data
from quiz_brain import QuizBrain 

question_bank = []

for data in question_data:
    question = data["text"]
    answer = data["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions:

    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}. ")