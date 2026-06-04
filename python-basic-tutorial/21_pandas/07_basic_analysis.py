# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
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

import pandas as pd
students = pd.DataFrame({"marks": [80, 85, 90]})
print("Average marks:", students["marks"].mean())
print(students.describe())
