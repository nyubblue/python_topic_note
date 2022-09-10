from question_model import Question
# from data import question_data
from requests import *
from quiz_brain import QuizBrain
from ui import QuizzInterface

question_bank = []

parameters = {
    "amount": 10,
    "difficulty": "medium",
    "type": "boolean",
}

response = get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print("Start UI")
quiz_ui = QuizzInterface(quiz)
print("End UI")

# while quiz.still_has_questions():
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
