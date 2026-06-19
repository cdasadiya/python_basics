# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Python Memory Management Basics
# Learning Objective: Understand how Python stores and cleans up values.
# Short Explanation: Python automatically manages memory, so beginners focus on references, reuse, and avoiding unnecessary huge data.
# Expected Output:
# Same object before change: True
# Original list: [1, 2, 3]
# Copied list: [1, 2, 3, 4]
# Common Mistakes:
# - Do not use unclear names like x1 when a meaningful name is possible.
# - Remember that Python is case-sensitive, so age and Age are different names.
# Interview Questions:
# - What is Python Memory Management Basics?
# - Why is this topic useful in real programs?
# Best Practices:
# - Use clear names that explain the purpose of the value.
# - Keep examples small while learning, then combine concepts later.

# A list is an object stored in memory.
original_numbers = [1, 2, 3]

# This does not create a new list; it creates another name for the same list.
same_numbers = original_numbers
print("Same object before change:", same_numbers is original_numbers)

# copy() creates a separate list object, which is safer when you want independent data.
copied_numbers = original_numbers.copy()
copied_numbers.append(4)

print("Original list:", original_numbers)
print("Copied list:", copied_numbers)
