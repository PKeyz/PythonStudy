# TODO 4. asking the questions
# TODO 5. checking if the answer was correct
# TODO 6. checking if we're at the end of the quiz

# create class QuizBrain
# Write an __init__() method

class QuizBrain:
    def __init__(self, q_list: list):
        self.question_number: int = 0
        self.question_list: list = q_list
        self.score = 0

    # TODO 8. create method still_has_questions()
    # return bool depending on value of question_number
    # use while loop to show next question until the end
    def still_has_questions(self):
        if len(self.question_list) == self.question_number:
            self.print_score()
        return len(self.question_list) > self.question_number

    # TODO 7. retrieve item at current question_number from question_list.
    # use input() to show the user the Question text and ask for user's answer.
    def next_question(self):
        user_answer = input(f'Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False): ')
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1
        return user_answer

    def check_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('You got it wrong!')
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is : {self.score}/{self.question_number + 1}\n')

    def print_score(self):
        print(f'You"ve completed the quiz\nYour final score was: {self.score}/{self.question_number}')