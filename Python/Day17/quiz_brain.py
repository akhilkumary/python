class QuizBrain:
    def __init__(self, que_list):
        self.question_number = 0        
        self.question_list = que_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        

    def check_answer(self, response):
        current_question = self.question_list[self.question_number - 1]
        right_or_wrong = ''
        if current_question.answer.lower() == response.lower():
            right_or_wrong = 'right'
            self.update_score()
        else:
            right_or_wrong = 'wrong'
        print(f"You got it {right_or_wrong}!")
        print(f"The correct answer was: {current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
        
    def update_score(self):
        self.score += 1

    def print_final_msg(self):
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{len(self.question_list)}")