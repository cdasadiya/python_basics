# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Default Parameter
# Learning Objective: Use a default value when no argument is given.
# Short Explanation: Default parameters make functions easier to call.
# Expected Output:
# Hello, friend!
# Hello, Sam!
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Default Parameter?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

def greet(name="friend"):
    print(f"Hello, {name}!")
greet()
greet("Sam")
