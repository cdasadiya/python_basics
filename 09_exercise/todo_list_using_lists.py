# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Todo List Using Lists
# Learning Objective: Practice list operations with a simple todo example.
# Short Explanation: This is not a full project; it is one topic exercise showing list add/remove/display.
# Expected Output:
# Todo items: ['study Python', 'practice loops']
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Todo List Using Lists?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

todos = []
todos.append("study Python")
todos.append("practice loops")
print("Todo items:", todos)
completed = todos.pop(0)
print("Completed:", completed)
print("Remaining:", todos)
