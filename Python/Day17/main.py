from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []

for que in question_data:
    questions.append(Question(que['text'], que['answer']))

new_quiz = QuizBrain(questions)

while new_quiz.still_has_questions():
    response = new_quiz.next_question()
    new_quiz.check_answer(response)
    
new_quiz.print_final_msg()