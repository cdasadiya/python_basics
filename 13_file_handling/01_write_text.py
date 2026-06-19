# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Write Text File
# Learning Objective: Write text to a file.
# Short Explanation: File handling lets programs save data permanently.
# Expected Output:
# File written successfully.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Write Text File?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

from pathlib import Path
file_path = Path(__file__).with_name("sample.txt")
file_path.write_text("Hello file!\n", encoding="utf-8")
print("File written successfully.")
