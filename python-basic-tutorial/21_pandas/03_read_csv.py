# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Pandas Read CSV
# Learning Objective: Read CSV into a DataFrame.
# Short Explanation: read_csv loads spreadsheet-style data.
# Expected Output:
# Alex
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Pandas Read CSV?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

from pathlib import Path
import pandas as pd
file_path = Path(__file__).with_name("students_pandas.csv")
file_path.write_text("name,marks\nAlex,90\nMaya,85\n", encoding="utf-8")
students = pd.read_csv(file_path)
print(students)
