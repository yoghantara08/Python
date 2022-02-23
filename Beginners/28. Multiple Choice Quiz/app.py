from Question import Question

question_prompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Violet\n(c) Purple\n\n",
    "What color are Bananas?\n(a) Black\n(b) Yellow/Green\n(c) White\n\n",
    "What color are Strawberries?\n(a) Red\n(b) Green\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)