# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Custom Exception
# Learning Objective: Create your own exception type.
# Short Explanation: Custom exceptions give meaningful names to special error cases.
# Expected Output:
# Age cannot be negative.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Custom Exception?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

class NegativeAgeError(Exception):
    pass

age = -1
try:
    if age < 0:
        raise NegativeAgeError("Age cannot be negative.")
except NegativeAgeError as error:
    print(error)
