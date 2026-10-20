"""Project 3: Multiple-Choice Quiz
Concepts: lists, dictionaries, loops, conditions and score tracking.
"""

QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"a": "func", "b": "def", "c": "function", "d": "define"},
        "answer": "b",
    },
    {
        "question": "Which data type stores True or False?",
        "options": {"a": "str", "b": "int", "c": "bool", "d": "list"},
        "answer": "c",
    },
    {
        "question": "Which symbol checks equality?",
        "options": {"a": "=", "b": "==", "c": "!=", "d": ">"},
        "answer": "b",
    },
    {
        "question": "What does len([4, 8, 12]) return?",
        "options": {"a": "2", "b": "3", "c": "4", "d": "24"},
        "answer": "b",
    },
    {
        "question": "Which loop is commonly used to iterate over a list?",
        "options": {"a": "for", "b": "switch", "c": "repeat-until", "d": "select"},
        "answer": "a",
    },
]


def main():
    score = 0
    print("Welcome to the Python Quiz!")
    print("Enter a, b, c or d for each question.\n")

    for number, item in enumerate(QUESTIONS, start=1):
        print(f"Q{number}. {item['question']}")
        for key, option in item["options"].items():
            print(f"  {key}) {option}")

        while True:
            answer = input("Your answer: ").strip().lower()
            if answer in item["options"]:
                break
            print("Please enter a, b, c or d.")

        if answer == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            correct = item["options"][item["answer"]]
            print(f"Not quite. Correct answer: {correct}\n")

    print("=== QUIZ RESULT ===")
    print(f"Score: {score}/{len(QUESTIONS)}")
    print(f"Percentage: {score / len(QUESTIONS) * 100:.1f}%")


if __name__ == "__main__":
    main()
