# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Local and Global Scope
# Learning Objective: Understand where variables can be used.
# Short Explanation: Local variables live inside functions; global variables live outside.
# Expected Output:
# Global: Python
# Local: Java
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Local and Global Scope?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

language = "Python"
def show_language():
    local_language = "Java"
    print("Global:", language)
    print("Local:", local_language)
show_language()
