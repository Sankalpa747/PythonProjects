# Imports
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Question bank
question_bank = []
for question in question_data:
    """Iterate through each question and construct Question objects."""
    question_bank.append(Question(question["text"], question["answer"]))

# Quiz brain
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    """Ask all the questions in the question bank."""
    quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
