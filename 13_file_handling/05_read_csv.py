# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Read CSV File
# Learning Objective: Read table data from CSV.
# Short Explanation: csv.DictReader reads each row as a dictionary.
# Expected Output:
# Alex scored 90
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Read CSV File?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

import csv
from pathlib import Path
file_path = Path(__file__).with_name("students.csv")
if not file_path.exists():
    file_path.write_text("name,marks\nAlex,90\n", encoding="utf-8")
with file_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} scored {row['marks']}")
