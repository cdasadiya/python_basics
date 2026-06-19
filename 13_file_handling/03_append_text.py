# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Append Text File
# Learning Objective: Add text to an existing file.
# Short Explanation: Append mode keeps old content and adds new content at the end.
# Expected Output:
# Text appended successfully.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Append Text File?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

from pathlib import Path
file_path = Path(__file__).with_name("sample.txt")
with file_path.open("a", encoding="utf-8") as file:
    file.write("New line added.\n")
print("Text appended successfully.")
