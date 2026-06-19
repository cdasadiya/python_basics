# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
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

import importlib.util

# This chapter uses the third-party package "requests".
# If it is not installed yet, the file still exits cleanly and tells the learner what to do.
if importlib.util.find_spec("requests") is None:
    print("This example needs the requests package.")
    print("Install it with: python -m pip install requests")
    raise SystemExit(0)

import requests
# Create a request object without sending internet traffic.
request = requests.Request("GET", "https://example.com/")
# prepare() builds the final request details safely.
prepared = request.prepare()
print("Prepared URL:", prepared.url)
