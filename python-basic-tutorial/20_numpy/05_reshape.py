# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
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

import numpy as np
numbers = np.array([1, 2, 3, 4, 5, 6])
print(numbers.reshape(3, 2))
