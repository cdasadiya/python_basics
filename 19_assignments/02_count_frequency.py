# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Count Frequency
# Learning Objective: Count how often each value appears.
# Short Explanation: Frequency means number of occurrences.
# Expected Output:
# {'apple': 2, 'banana': 1}
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Count Frequency?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

fruits = ["apple", "banana", "apple"]
frequency = {}
for fruit in fruits:
    frequency[fruit] = frequency.get(fruit, 0) + 1
print(frequency)
