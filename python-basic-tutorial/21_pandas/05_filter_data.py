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

import importlib.util

# This chapter uses the third-party package "pandas".
# If it is not installed yet, the file still exits cleanly and tells the learner what to do.
if importlib.util.find_spec("pandas") is None:
    print("This example needs the pandas package.")
    print("Install it with: python -m pip install pandas")
    raise SystemExit(0)

import pandas as pd
# A DataFrame stores data in rows and columns, like a spreadsheet.
students = pd.DataFrame({"name": ["Alex", "Maya"], "marks": [90, 35]})
passed = students[students["marks"] >= 40]
print(passed)
