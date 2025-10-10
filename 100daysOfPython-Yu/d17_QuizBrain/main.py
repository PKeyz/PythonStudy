import data
import question_model
import quiz_brain

# new_question = question_model.Question()
question_bank = []
question_counter: int = 0

quiz = quiz_brain.QuizBrain(question_bank)


# TODO 1. with custom names -> generate custom Obj. QUESTION with different text/answer
# TODO 2. append Obj. QUESTION to question_bank[]
def generate_question_objects():
    for question_element in data.question_data:
        question_text: str = question_element['question']
        question_answer: bool = question_element['correct_answer']
        question_object = question_model.Question(question_text, question_answer)
        question_bank.append(question_object)


# TODO 3. print questions and answers
def print_questions():
    counter = 0
    for question in question_bank:
        print(question_bank[counter].text)
        print(question_bank[counter].answer)
        counter += 1


generate_question_objects()

while quiz.still_has_questions():
    quiz.next_question()
