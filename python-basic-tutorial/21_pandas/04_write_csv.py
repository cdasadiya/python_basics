# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
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
import pandas as pd
file_path = Path(__file__).with_name("output_pandas.csv")
students = pd.DataFrame({"name": ["Alex"], "marks": [90]})
students.to_csv(file_path, index=False)
print("CSV saved with pandas.")
