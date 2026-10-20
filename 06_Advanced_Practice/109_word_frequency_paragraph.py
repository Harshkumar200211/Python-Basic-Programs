"""109. Count Word Frequency in a Paragraph."""

import re

paragraph = "Python is easy. Python is useful and Python is popular."
words = re.findall(r"\b[a-zA-Z]+\b", paragraph.lower())
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in sorted(frequency.items()):
    print(word, ":", count)
