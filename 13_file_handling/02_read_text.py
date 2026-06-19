# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Read Text File
# Learning Objective: Read text from a file.
# Short Explanation: Reading files loads saved data back into a program.
# Expected Output:
# Hello file!
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Read Text File?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

from pathlib import Path
file_path = Path(__file__).with_name("sample.txt")
if not file_path.exists():
    file_path.write_text("Hello file!\n", encoding="utf-8")
content = file_path.read_text(encoding="utf-8")
print(content.strip())
