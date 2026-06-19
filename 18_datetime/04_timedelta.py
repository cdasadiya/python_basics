# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: timedelta
# Learning Objective: Add or subtract time durations.
# Short Explanation: timedelta represents a length of time.
# Expected Output:
# Tomorrow: 2026-06-05
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is timedelta?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

from datetime import date, timedelta
today = date(2026, 6, 4)
tomorrow = today + timedelta(days=1)
print("Tomorrow:", tomorrow)
