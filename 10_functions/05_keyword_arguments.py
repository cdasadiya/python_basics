# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Keyword Arguments
# Learning Objective: Pass arguments by name.
# Short Explanation: Keyword arguments make function calls clear.
# Expected Output:
# Maya is 16 years old.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Keyword Arguments?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

def show_student(name, age):
    print(f"{name} is {age} years old.")
show_student(age=16, name="Maya")
