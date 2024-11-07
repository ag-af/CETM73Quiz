import random

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
                        print("Correct!")
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
        print(f"\nHighest scorer: {highest_scorer} with {self.scores[highest_scorer]} points!")
        print(f"Average score of all users: {average_score:.2f}")


def main():
    quiz = Quiz()
    quiz.add_question("What is the only country that starts with O?", "Oman")
    quiz.add_question("What is the capital of Japan?", "Tokyo")
    quiz.add_question("What is the smallest country in the world?", "Vatican City")
    quiz.add_question("What is the biggest country in South America?", "Brazil")
    quiz.add_question("What is the oldest recorded town in the UK?", "Colchester")
    quiz.add_question("Which country has the largest population?", "China")
    quiz.add_question("To which country do the Canary Islands belong?", "Spain")
    quiz.add_question("Which African country has the largest population?", "Nigeria")
    quiz.add_question("What is the tallest mountain in the world?", "Mount Everest")
    quiz.add_question("On the London Tube network, which is the only station to begin with the letter 'I'?", "Ickenham")

    while True:
        username = input("\nEnter your name: ").strip()
        if username == "":
            print("Name cannot be empty. Please enter a name")
            continue

        quiz.take_quiz(username)

        continue_quiz = input("\nDoes anyone else want to play the quiz? (yes/no): ").strip().lower()
        if continue_quiz != "yes":
            break

    quiz.display_results()

if __name__ == "__main__":
    main()