# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: List copy()
# Learning Objective: Make a separate list copy.
# Short Explanation: copy() avoids changing the original accidentally.
# Expected Output:
# Original: ['A', 'B']
# Copy: ['A', 'B', 'C']
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is List copy()?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

original = ["A", "B"]
copy_list = original.copy()
copy_list.append("C")
print("Original:", original)
print("Copy:", copy_list)
