# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Basic Data Analysis
# Learning Objective: Use describe and simple statistics.
# Short Explanation: Pandas can quickly summarize data.
# Expected Output:
# Average marks: 85.0
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Basic Data Analysis?
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
students = pd.DataFrame({"marks": [80, 85, 90]})
print("Average marks:", students["marks"].mean())
print(students.describe())
