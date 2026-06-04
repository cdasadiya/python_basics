# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Array Shape
# Learning Objective: Read array dimensions.
# Short Explanation: shape tells rows and columns.
# Expected Output:
# (2, 3)
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Array Shape?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

import importlib.util

# This chapter uses the third-party package "numpy".
# If it is not installed yet, the file still exits cleanly and tells the learner what to do.
if importlib.util.find_spec("numpy") is None:
    print("This example needs the numpy package.")
    print("Install it with: python -m pip install numpy")
    raise SystemExit(0)

import numpy as np
# A matrix is a two-dimensional array with rows and columns.
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)
