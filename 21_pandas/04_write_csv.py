# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Pandas Write CSV
# Learning Objective: Write DataFrame to CSV.
# Short Explanation: to_csv saves table data.
# Expected Output:
# CSV saved with pandas.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Pandas Write CSV?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

from pathlib import Path
import importlib.util

# This chapter uses the third-party package "pandas".
# If it is not installed yet, the file still exits cleanly and tells the learner what to do.
if importlib.util.find_spec("pandas") is None:
    print("This example needs the pandas package.")
    print("Install it with: python -m pip install pandas")
    raise SystemExit(0)

import pandas as pd
file_path = Path(__file__).with_name("output_pandas.csv")
# A DataFrame stores data in rows and columns, like a spreadsheet.
students = pd.DataFrame({"name": ["Alex"], "marks": [90]})
students.to_csv(file_path, index=False)
print("CSV saved with pandas.")
