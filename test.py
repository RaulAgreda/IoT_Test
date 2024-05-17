import json
import os
from termcolor import colored
import random

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def LoadQuestions(questions_folder):
    question_set = []

    # Load all the questions from the test folder
    for filename in os.listdir(TEST_FOLDER):
        with open(os.path.join(TEST_FOLDER, filename), "r") as f:
            data = json.load(f)
            question_set.append({"title": filename.removesuffix(".json"), "questions": data})
    # Sort by title
    question_set.sort(key=lambda x: x["title"])
    return question_set

def InputAnswer():
    answer = None
    while answer not in ['a', 'b', 'c', 'd']:
        answer = input("Respuesta: ")
    return answer

def DisplayQuestion(question, id):
    questionOrder = ['a', 'b', 'c', 'd']
    # Print question
    print("Pregunta " + str(id) + ":\n" + question["question"])
    # Print options
    for option in questionOrder:
        print(option + ")", question[option])

    return InputAnswer() == question["answer"]

def DisplayQuestionSet(question_set):
    totalScore = 0
    maxScore = 0
    for question_theme in question_set:
        i = 0
        score = 0
        title = question_theme["title"].upper().replace("_", " ")
        shuffle = question_theme["questions"].copy()
        random.shuffle(shuffle)
        for question in shuffle:
            i += 1
            print(colored(title, "cyan"))
            if DisplayQuestion(question, i):
                print(colored("¡Correcto!", "green"))
                score += 1
            else:
                print(colored("¡Incorrecto!", "red"))
                print("La respuesta correcta era la " + question["answer"] + ")")
            input("Presiona Enter para continuar...")
            ClearScreen()
        print(f"Has sacado un {score}/{i} en el tema {title}")
        totalScore += score
        maxScore += i
        input("Presiona Enter para continuar...")
        ClearScreen()
    print(f"Has sacado un {totalScore}/{maxScore} en total, tienes un {round(totalScore/maxScore*10, 2)}")

if __name__ == "__main__":
    TEST_FOLDER = "./test_questions"

    ClearScreen()

    question_set = LoadQuestions(TEST_FOLDER)
    DisplayQuestionSet(question_set)
