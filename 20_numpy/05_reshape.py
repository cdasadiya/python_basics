# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Reshape Array
# Learning Objective: Change array dimensions.
# Short Explanation: reshape changes layout without changing values.
# Expected Output:
# [[1 2]
#  [3 4]
#  [5 6]]
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Reshape Array?
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
# np.array() converts a Python list into a NumPy array.
numbers = np.array([1, 2, 3, 4, 5, 6])
print(numbers.reshape(3, 2))
