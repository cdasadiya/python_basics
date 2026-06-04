# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Python Coding Standards PEP8
# Learning Objective: Write readable Python code using common style rules.
# Short Explanation: PEP8 is Python guidance for clean names, spacing, indentation, and organization.
# Expected Output:
# Total marks: 175
# Common Mistakes:
# - Do not use unclear names like x1 when a meaningful name is possible.
# - Remember that Python is case-sensitive, so age and Age are different names.
# Interview Questions:
# - What is Python Coding Standards PEP8?
# - Why is this topic useful in real programs?
# Best Practices:
# - Use clear names that explain the purpose of the value.
# - Keep examples small while learning, then combine concepts later.

# Good variable names describe the data clearly.
math_marks = 90
science_marks = 85

# Spaces around operators make expressions easier to read.
total_marks = math_marks + science_marks

# A small function with one clear job is easy to test and understand.
def show_total_marks(total):
    print("Total marks:", total)


# Two blank lines before a top-level function is a common PEP8 style rule.
show_total_marks(total_marks)
