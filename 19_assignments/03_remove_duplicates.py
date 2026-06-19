# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Remove Duplicates
# Learning Objective: Remove repeated values while keeping order.
# Short Explanation: This assignment uses a set to remember what already appeared.
# Expected Output:
# [1, 2, 3, 4]
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Remove Duplicates?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

numbers = [1, 2, 2, 3, 1, 4]
unique_numbers = []
seen = set()
for number in numbers:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)
print(unique_numbers)
