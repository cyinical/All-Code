question_prompts = [

"What is the best car in Rockat League?\n(a) Octane\n(b)Dominus",



"What is the best car for 1v1?\n(a) Merc\n(b)Fennec",



"What is the best competitive game mode?\n(a) 1v1\n(b)2v2\n(c)3v3",



"What is the best extra games mode?\n(a) Rumble\n(b)Dropshot\n(c)Hoops\(d)Snowday",



"What is the meme car for Rocket League?\n(a) Scarab\n(b)Merc",



"What is the popular freestylers car?\n(a) Breakout\n(b)Dominus",



"What is the best Pro Esports team in Rocket League?\n(a) NRG\n(b)SSG",



"What is the harder freestyle shot?\n(a) Ceiling shot musty flick double tap\n(b)Double flip resets double tap",



"Who is the best Rocket Player?\n(a) JSTN\n(b)Arsenal",



"Who is the better freestyler?\n(a) Pulse Evample\n(b)Pulse Henkovic",



]







questions = [



Question(question_prompts[0], "a"),

Question(question_prompts[1], "b"),



Question(question_prompts[2], "b"),



Question(question_prompts[3], "c"),



Question(question_prompts[4], "a"),



Question(question_prompts[5], "b"),



Question(question_prompts[6], "a"),



Question(question_prompts[7], "b"),



Question(question_prompts[8], "a"),



Question(question_prompts[9], "a"),
]




def run_quiz(questions):



score = 0



for question in questions:



answer = input (question.prompt)



if answer == question.answer:



score += 1



print("you got", score, "out of", len(questions))
