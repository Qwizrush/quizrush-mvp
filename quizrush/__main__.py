from .quiz import Quiz
import os

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    questions_path = os.path.join(base_dir, "questions.json")
    quiz = Quiz(questions_path)
    quiz.run()
