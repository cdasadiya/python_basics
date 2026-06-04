# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Pandas DataFrame
# Learning Objective: Create table data.
# Short Explanation: A DataFrame is like a spreadsheet table.
# Expected Output:
# name  marks
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Pandas DataFrame?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

import pandas as pd
students = pd.DataFrame({"name": ["Alex", "Maya"], "marks": [90, 85]})
print(students)
