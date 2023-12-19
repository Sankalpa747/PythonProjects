# Quiz brain class
class QuizBrain:

    def __init__(self, question_list):
        """Constructor of the QuizBrain class."""
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        """Responsible for prompting the questions."""
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        """Checks whether there are more questions left and returns True or False."""
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        """Check whether the user answer is correct after comparing with the correct answer.
           Internally handle the quiz score."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Yot it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}\n")

