import random
from multiprocessing.managers import Value


class Quiz:
    def __init__(self):
        self.questions = []
        self.scores = {}

        def add_question(self, question, answer):
            self.questions.append((question, answer))

            def take_quiz(self, username):
                score = 0

                questions_asked = random.sample(self.questions, len(self.questions))
                for i, (question, answer) in enumerate(questions_asked, 1):
                    while True:
                        try:
                            user_answer = input(f"Q{i}: {question} ").strip()
                            if not user_answer:
                                raise ValueError("Answer cannot be empty. Please enter an answer.")

                            if user_answer.lower() == answer.lower():
                                score += 1
                            else:
                                print(f"Incorrect! The correct answer was: {answer}")
                                break
                        except ValueError as e:
                            print(e)

                            print(f"\n{username}, you scored {score} out of {len(self.questions)}")
                            self.scores[username] = score

                            def display_results(self):
                                print("\n Quiz Results")
                                for user, score in self.scores.items():
                                    print(f"{user}: {score} points")
                                    highest_scorer = max(self.scores, key=self.scores.get)
                                    average_score = sum(self.scores.values()) / len(self.scores)

                                    print(f"\n Highest scorer: {highest_scorer} with {self.scores[highest_scorer]} points!")
                                    print(f"Average score of all users: {average_score:.2f}")