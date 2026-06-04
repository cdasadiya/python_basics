# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: os Module
# Learning Objective: Interact with the operating system.
# Short Explanation: os can read environment info and paths.
# Expected Output:
# Current folder name: 17_modules
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is os Module?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

import os
current_folder = os.path.basename(os.path.dirname(__file__))
print("Current folder name:", current_folder)
