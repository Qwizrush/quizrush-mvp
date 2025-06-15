import json
import os

class Quiz:
    def __init__(self, questions_file: str):
        self.questions_file = questions_file
        self.questions = []
        self.load_questions()

    def load_questions(self):
        if not os.path.exists(self.questions_file):
            raise FileNotFoundError(f"Questions file {self.questions_file} not found")
        with open(self.questions_file, "r", encoding="utf-8") as f:
            self.questions = json.load(f)
        if not isinstance(self.questions, list):
            raise ValueError("Questions data must be a list")

    def run(self):
        if not self.questions:
            print("No questions available.")
            return
        score = 0
        for index, q in enumerate(self.questions, start=1):
            print(f"{index}. {q['question']}")
            for i, option in enumerate(q['options'], start=1):
                print(f"   {i}. {option}")
            answer = input("Your answer: ")
            try:
                answer_index = int(answer) - 1
            except ValueError:
                print("Invalid input. Skipping question.")
                continue
            if answer_index == q.get('answer'):
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect! Correct answer: {q['options'][q['answer']]}\n")
        print(f"Quiz finished! Your score: {score}/{len(self.questions)}")

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    questions_path = os.path.join(base_dir, "questions.json")
    quiz = Quiz(questions_path)
    quiz.run()
