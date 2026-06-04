# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: if elif else and Nested Conditions
# Learning Objective: Check many conditions including one condition inside another.
# Short Explanation: elif means otherwise if. Nested conditions are if statements inside if statements.
# Expected Output:
# Grade: A
# Excellent work!
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is if elif else and Nested Conditions?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

marks = 91
if marks >= 90:
    print("Grade: A")
    if marks >= 95:
        print("Outstanding score!")
    else:
        print("Excellent work!")
elif marks >= 75:
    print("Grade: B")
else:
    print("Keep improving!")
