"""91. Explore basic operating-system information with os."""

import os

print("Current working directory:")
print(os.getcwd())

print("\nItems in the current folder:")
for item in sorted(os.listdir("."))[:20]:
    print(item)

print("\nIs README.md present?", os.path.exists("README.md"))
