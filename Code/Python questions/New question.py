class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt

        self.answer = answer

question_prompts = [
    "Hong Kong is a capitalist country.\nTrue or False?\n",
    "How many MB (Megabytes) are in a GB (Gigabyte) in binary.\n(A): 1000 (B): 1030 (C): 1024\n",
]

questions = [
    Question(question_prompts[0], "True"),
    Question(question_prompts[1], "C"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    
    print("Score", score, "out of", len(questions))

run_quiz(questions)