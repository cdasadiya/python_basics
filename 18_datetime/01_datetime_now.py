# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: datetime.now()
# Learning Objective: Get the current date and time.
# Short Explanation: datetime.now() reads the current clock time.
# Expected Output:
# Current date and time: ...
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is datetime.now()?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

from datetime import datetime
now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M"))
