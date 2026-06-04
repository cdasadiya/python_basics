# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Write CSV File
# Learning Objective: Write table data to CSV.
# Short Explanation: CSV files store rows and columns and open in spreadsheet apps.
# Expected Output:
# CSV written successfully.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Write CSV File?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

import csv
from pathlib import Path
file_path = Path(__file__).with_name("students.csv")
with file_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "marks"])
    writer.writerow(["Alex", 90])
print("CSV written successfully.")
