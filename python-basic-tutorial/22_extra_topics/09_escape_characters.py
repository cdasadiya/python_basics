# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Escape Characters
# Learning Objective: Use special characters inside strings.
# Short Explanation: Escape characters start with a backslash and help write tabs, new lines, quotes, and backslashes inside text.
# Expected Output:
# Line 1
# Line 2
# She said, "Python is fun!"
# Name:    Alex
# Common Mistakes:
# - Do not forget the backslash before special characters.
# - Remember that escape characters work inside strings, not as normal text outside strings.
# Interview Questions:
# - What is an escape character?
# - Why would you use \n, \t, or \" in a string?
# Best Practices:
# - Use escape characters only when they make the text clearer.
# - Use triple-quoted strings for long multi-line text.

# \n creates a new line inside a string.
two_lines = "Line 1\nLine 2"

# \" lets us place double quotes inside a double-quoted string.
quoted_text = "She said, \"Python is fun!\""

# \t creates a tab space, often used to align simple text output.
tabbed_text = "Name:\tAlex"

print(two_lines)
print(quoted_text)
print(tabbed_text)
