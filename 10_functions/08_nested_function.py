# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Nested Function
# Learning Objective: Create a function inside another function.
# Short Explanation: Nested functions help organize helper logic.
# Expected Output:
# Outer function
# Inner function
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Nested Function?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer()
