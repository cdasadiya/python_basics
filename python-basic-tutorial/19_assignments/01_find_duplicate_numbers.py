# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Find Duplicate Numbers
# Learning Objective: Practice finding repeated numbers.
# Short Explanation: Duplicates are values that appear more than once.
# Expected Output:
# Duplicates: [2, 4]
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Find Duplicate Numbers?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

numbers = [1, 2, 2, 3, 4, 4, 5]
seen = set()
duplicates = []
for number in numbers:
    if number in seen and number not in duplicates:
        duplicates.append(number)
    seen.add(number)
print("Duplicates:", duplicates)
