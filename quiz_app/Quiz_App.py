from Question import Question

qn_prompts = [
    "Most Populated country in the world?\n(A) China\n(B) India\n(C) USA\n\n",
    "Colour of human blood?\n(A) Red\n(B) Blue\n(C) Yellow\n\n",
    "No.of bones in human skeleton?\n(A) 260\n(B) 620\n(C) 206\n\n",
]

questions = [
    Question(qn_prompts[0],"B"),
    Question(qn_prompts[1],"A"),
    Question(qn_prompts[2],"C")
]

def run_quiz(questions):
    score = 0
    for qn in questions:
        ans = input(qn.prompt)
        if ans == qn.answer:
            score += 1
    print("Quiz completed... Your score is "+str(score)+"/"+str(len(questions)))


run_quiz(questions)