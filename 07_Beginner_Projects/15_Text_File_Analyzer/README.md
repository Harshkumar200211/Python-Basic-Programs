# Project: Text File Analyzer

## What this project does

Analyze a text file and report lines, words, characters, unique words and the most frequent words.

## Python concepts used

pathlib, file handling, strings, regular expressions and collections.Counter.

## How it works, step by step

1. Enter a text file path or press Enter to use a sample file.
2. Create sample_text.txt automatically if the default is selected and the file does not exist.
3. Read the text using UTF-8 encoding.
4. Count lines, words, characters and unique words.
5. Display the five most frequent words.

## Files used

- `main.py` — Reads and analyzes the text.
- `sample_text.txt` — Generated automatically when the default file is selected.

## How to run

1. Install Python 3.
2. Open this project folder in a terminal.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Learning note

Character count includes spaces and line breaks. The regular expression uses a simple word definition for learning.

After the first run, change some inputs and explain how the code uses each listed concept.
