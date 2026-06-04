# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: json Module
# Learning Objective: Convert between dictionaries and JSON text.
# Short Explanation: JSON is a common format for APIs and configuration.
# Expected Output:
# {"name": "Alex", "age": 16}
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is json Module?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

import json
student = {"name": "Alex", "age": 16}
json_text = json.dumps(student)
print(json_text)
print(json.loads(json_text)["name"])
