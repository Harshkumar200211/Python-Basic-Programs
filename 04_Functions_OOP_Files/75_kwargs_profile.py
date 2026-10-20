"""75. Function with **kwargs

Python practice program 75 of 100.
"""

def show_profile(**details):
    for key, value in details.items():
        print(key, ":", value)

show_profile(name="Aman", age=20, course="Python")
