from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = [Question(q["text"], q["answer"]) for q in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
