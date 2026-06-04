# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Filter Data
# Learning Objective: Select rows that match a condition.
# Short Explanation: Filtering is like asking a table a question.
# Expected Output:
# Alex
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Filter Data?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

import pandas as pd
students = pd.DataFrame({"name": ["Alex", "Maya"], "marks": [90, 35]})
passed = students[students["marks"] >= 40]
print(passed)
