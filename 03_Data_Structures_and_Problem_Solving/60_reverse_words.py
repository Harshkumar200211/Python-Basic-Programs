"""60. Reverse the Order of Words

Python practice program 60 of 100.
"""

sentence = input("Enter a sentence: ")
words = sentence.split()
print(" ".join(words[::-1]))
