```
import random

class Quiz:
    def __init__(self, discipline):
        self.discipline = discipline
        self.questions = {
            "Matemática": [
                {"question": "What is the value of x in the equation 2x + 5 = 11?",
                 "options": ["1", "2", "3", "4", "5"],
                 "answer": "3",
                 "feedback": "Correct!"},
                {"question": "What is the value of y in the equation y^2 + 4y - 5 = 0?",
                 "options": ["1", "2", "3", "4", "5"],
                 "answer": "2",
                 "feedback": "Correct!"},
                # ...
            },
            "Sociologia": [
                {"question": "What is the definition of sociology?",
                 "options": ["1", "2", "3", "4", "5"],
                 "answer": "2",
                 "feedback": "Correct!"},
                {"question": "Who is the founder of sociology?",
                 "options": ["1", "2", "3", "4", "5"],
                 "answer": "1",
                 "feedback": "Correct!"},
                # ...
            },
            "Filosofia": [
                {"question": "Who is the father of philosophy?",
                 "options": ["1", "2", "3", "4", "5"],
                 "answer": "1",
                 "feedback": "Correct!"},
                {"question": "What is the meaning of the word 'philosophy'?",
                 "options": ["1", "2", "3", "4", "5"],
                 "answer": "2",
                 "feedback": "Correct!"},
                # ...
            ]
        }
        self.score = 0
        self.attempts = 0
        self.user_answers = []

    def ask_question(self):
        question = random.choice(self.questions[self.discipline])
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        answer = input("Enter your answer: ")
        self.user_answers.append(answer)
        if answer == question["answer"]:
            self.score += 100
            print(question["feedback"])
        else:
            self.attempts += 1
            print("Incorrect. You have 1 more chance.")
            answer = input("Enter your answer: ")
            self.user_answers.append(answer)
            if answer == question["answer"]:
                self.score += 70
                print(question["feedback"])
            else:
                print(question["feedback"])
                self.score -= 20

    def show_score(self):
        print(f"Your score is: {self.score}")

    def show_ranking(self, scores):
        print("Ranking:")
        for i, (user, score) in enumerate(scores.items()):
            print(f"{i+1}. {user} - {score}")

    def run(self):
        scores = {}
        while True:
            print("1. Start quiz")
            print("2. Show scores")
            print("3. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.score = 0
                self.attempts = 0
                self.user_answers = []
                for _ in range(10):
                    self.ask_question()
                scores[self.discipline] = self.score
            elif choice == "2":
                self.show_score()
                self.show_ranking(scores)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Choose a discipline:")
    print("1. Matemática")
    print("2. Sociologia")
    print("3. Filosofia")
    choice = input("Enter your choice: ")
    if choice == "1":
        discipline = "Matemática"
    elif choice == "2":
        discipline = "Sociologia"
    elif choice == "3":
        discipline = "Filosofia"
    else:
        print("Invalid choice. Please try again.")
        exit()
    quiz = Quiz(discipline)
    quiz.run()
```

