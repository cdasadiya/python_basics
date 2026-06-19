# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Nested Loops
# Learning Objective: Use a loop inside another loop.
# Short Explanation: Nested loops are helpful for grids, tables, and combinations.
# Expected Output:
# Row 1 Seat 1
# Row 1 Seat 2
# ...
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Nested Loops?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

for row in range(1, 3):
    for seat in range(1, 3):
        print(f"Row {row} Seat {seat}")
