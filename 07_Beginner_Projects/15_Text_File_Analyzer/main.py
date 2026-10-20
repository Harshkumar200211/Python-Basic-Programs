"""Project 15: Text File Analyzer
Counts lines, words, characters and frequent words in a text file.
Concepts: pathlib, file handling, strings, regular expressions and Counter.
"""

import re
from collections import Counter
from pathlib import Path

SAMPLE_TEXT = """Python is a readable programming language.
Python supports functions, modules and classes.
Practice Python regularly to improve programming logic.
"""


def create_sample_file(path):
    path.write_text(SAMPLE_TEXT, encoding="utf-8")
    print(f"Created a sample text file: {path}")


def analyze_file(path):
    text = path.read_text(encoding="utf-8")
    words = re.findall(r"[A-Za-z0-9']+", text.lower())
    word_counts = Counter(words)

    print("\n=== TEXT ANALYSIS ===")
    print("File:", path)
    print("Lines:", len(text.splitlines()))
    print("Words:", len(words))
    print("Characters (including spaces and line breaks):", len(text))
    print("Unique words:", len(word_counts))
    print("\nTop 5 frequent words:")
    for word, count in word_counts.most_common(5):
        print(f"{word}: {count}")


def main():
    entered_path = input(
        "Enter text file path (press Enter to use sample_text.txt): "
    ).strip()
    path = Path(entered_path) if entered_path else Path(__file__).with_name("sample_text.txt")

    if not path.exists() and not entered_path:
        create_sample_file(path)

    try:
        if not path.is_file():
            print("The path is not a file.")
            return
        analyze_file(path)
    except (OSError, UnicodeError) as error:
        print("Could not read the file:", error)


if __name__ == "__main__":
    main()
