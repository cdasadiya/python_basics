# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: requests Module
# Learning Objective: Understand third-party package usage.
# Short Explanation: requests helps call websites and APIs; this demo prepares a request without using the network.
# Expected Output:
# Prepared URL: https://example.com/
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is requests Module?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

import requests
request = requests.Request("GET", "https://example.com/")
prepared = request.prepare()
print("Prepared URL:", prepared.url)
