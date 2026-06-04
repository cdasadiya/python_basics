# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: groupby()
# Learning Objective: Group and summarize data.
# Short Explanation: groupby collects rows by category.
# Expected Output:
# A    85.0
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is groupby()?
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
data = pd.DataFrame({"section": ["A", "A", "B"], "marks": [80, 90, 70]})
print(data.groupby("section")["marks"].mean())
