class Quiz():
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

question_list=[
    "What is the full form of ABC? \n a.Apple ball cow \n b.abstract base class \n c.None \n d.error",
    "Which is dictionary? \n  a.dict \n  b.str \n  c.list \n  d.None ",
    "Dry in coding? \n  a.error \n  b.bug \n c.dont repeat yourself \n d.both"
]

quiz_list=[
    Quiz(question_list[0],"b"),
    Quiz(question_list[1],"a"),
    Quiz(question_list[2],"c")
]


def show(quiz_list): #i=Quiz(question_list[0],"b"),
    score = 0
    for i in quiz_list:
        user=input(f"{i.question}\n :") #b

        if user == i.answer:
            score += 1
        else:
            print(f"wrong answer your correct answer {i.answer}")

    print(f"your total score is {score}/{len(question_list)}")

show(quiz_list)