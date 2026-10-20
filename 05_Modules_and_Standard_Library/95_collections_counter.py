"""95. Count items efficiently with collections.Counter."""

from collections import Counter

sentence = input("Enter a sentence: ").lower()
words = sentence.split()
word_counts = Counter(words)

print("Word frequencies:")
for word, count in word_counts.most_common():
    print(word, ":", count)

numbers = [2, 3, 2, 5, 3, 2, 4, 3, 3]
print("Number frequencies:", Counter(numbers))
