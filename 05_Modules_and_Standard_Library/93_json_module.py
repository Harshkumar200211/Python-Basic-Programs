"""93. Convert Python data to and from JSON."""

import json

student = {
    "name": "Riya",
    "marks": [88, 92, 95],
    "passed": True
}

json_text = json.dumps(student, indent=4)
print("JSON text:")
print(json_text)

restored_data = json.loads(json_text)
print("Student name:", restored_data["name"])
print("Average marks:", sum(restored_data["marks"]) / len(restored_data["marks"]))
