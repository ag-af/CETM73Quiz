import random

class Quiz:
    def __init__(self):
        self.questions = []
        self.scores = {}

    def add_question(self, question, answer):
        self.questions.append((question, answer))

    def take_quiz(self, username, num_questions):
        score = 0

        questions_asked = random.sample(self.questions, min(num_questions, len(self.questions)))
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

        percentage = (score / len(questions_asked)) * 100
        print(f"\n{username}, you scored {score} out of {len(questions_asked)} ({percentage:.2f}%)")
        self.scores[username] = (score, percentage)

    def display_results(self):
        print("\n Quiz Results")
        for user, (score, percentage) in self.scores.items():
            point = "point" if score == 1 else "points"
            print(f"{user}: {score} {point} ({percentage:.2f}%)")
        highest_scorer = max(self.scores, key=lambda user: self.scores[user][0])
        highest_score, highest_percentage = self.scores[highest_scorer]
        highest_point = "point" if highest_score == 1 else "points"
        average_score = sum(score for score, _ in self.scores.values()) / len(self.scores)
        average_percentage = sum(percentage for _, percentage in self.scores.values()) / len(self.scores)

        print(f"\nHighest scorer: {highest_scorer} with {highest_score} {highest_point} ({highest_percentage:.2f}%)")
        print(f"Average score of all users: {average_score:.2f} points ({average_percentage:.2f}%)")


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
        try:
            num_questions = int(input(f"How many questions would you like to answer? (Max: {len(quiz.questions)}): "))
            if num_questions < 1 or num_questions > len(quiz.questions):
                print(f"Please enter a number between 1 and {len(quiz.questions)}.")
                continue
            break
        except ValueError:
            print("Invalid. Please enter a valid number.")

    while True:
        username = input("\nEnter your name: ").strip()
        if username == "":
            print("Name cannot be empty. Please enter a name")
            continue

        quiz.take_quiz(username, num_questions)

        continue_quiz = input("\nDoes anyone else want to play the quiz? (yes/no): ").strip().lower()
        if continue_quiz != "yes":
            break

    quiz.display_results()

if __name__ == "__main__":
    main()