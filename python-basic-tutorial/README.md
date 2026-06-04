# Python Basic Tutorial

A complete beginner-friendly Python learning repository for students starting from zero and growing toward intermediate Python skills.

## What is Programming?

Programming means writing step-by-step instructions that a computer can follow. A recipe tells a person how to cook; a program tells a computer how to calculate, decide, repeat, store, and display information.

## Why Python?

Python is popular because it is readable, beginner friendly, and powerful. It is used in web development, automation, data science, artificial intelligence, scripting, testing, and education.

## Installation Guide

1. Install Python 3.13 or newer from <https://www.python.org/downloads/>.
2. Confirm installation:

   ```bash
   python --version
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate it:

   ```bash
   source .venv/bin/activate
   ```

5. Install requirements:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Python vs Other Languages

| Feature | Python | Java | C++ | JavaScript |
|---|---|---|---|---|
| Beginner friendly | Very high | Medium | Lower | Medium |
| Syntax | Simple | Verbose | Complex | Flexible |
| Main uses | Data, web, automation, AI | Enterprise apps | Systems, games | Web browsers and servers |
| Speed | Good for most tasks | Fast | Very fast | Fast |

## Repository Structure

The repository is organized chapter-wise. Every concept has its own separate file and can be studied independently.

```text
python-basic-tutorial/
├── 01_introduction/
├── 02_datatypes/
├── 03_operators/
├── 04_conditions/
├── 05_loops/
├── 06_range/
├── 07_python2_vs_python3/
├── 08_lists/
├── 09_exercise/
├── 10_functions/
├── 11_strings/
├── 12_error_handling/
├── 13_file_handling/
├── 14_dictionary/
├── 15_tuple/
├── 16_sets/
├── 17_modules/
├── 18_datetime/
├── 19_assignments/
├── 20_numpy/
├── 21_pandas/
└── 22_extra_topics/
```

## How to Run Programs

Run any file with Python:

```bash
python 01_introduction/03_first_program.py
```

For NumPy, pandas, and requests examples, install requirements first:

```bash
python -m pip install -r requirements.txt
```

## Learning Path

1. Introduction and first program
2. Variables, constants, data types, input, and output
3. Operators and Boolean logic
4. Conditions and nested conditions
5. Loops, nested loops, break, continue, and pass
6. range and Python 2 vs Python 3 differences
7. Lists and list exercises
8. Functions, lambda, scope, and recursion
9. Strings and formatting
10. Error handling and custom exceptions
11. File handling and CSV files
12. Dictionaries, tuples, and sets
13. Modules, datetime, NumPy, and pandas
14. Extra professional topics: comments, PEP8, virtual environments, pip, and requirements files

## Assignments

- Find duplicate numbers.
- Count value frequency.
- Remove duplicates while keeping order.
- Modify examples by changing inputs and predicting output first.

## Interview Questions

1. What is the difference between a list and a tuple?
2. What is a dictionary and when would you use it?
3. What is the difference between `==` and `is`?
4. What is a function parameter?
5. What does `return` do?
6. What is recursion?
7. What is a custom exception?
8. What is the difference between Python 2 and Python 3 `print`?
9. What is a virtual environment?
10. Why should requirements be stored in `requirements.txt`?

## Python 2 vs Python 3 Summary

Use Python 3 for all new learning and development. Python 2 is outdated.

- Python 3 uses `print()` as a function.
- Python 3 uses `input()` instead of Python 2 `raw_input()`.
- Python 3 `range()` behaves efficiently like Python 2 `xrange()`.
- Python 3 strings are Unicode by default.
- Python 3 division with `/` returns a decimal result.

## Python Coding Standards (PEP8)

- Use clear names like `student_marks`, not `sm`.
- Use 4 spaces for indentation.
- Keep lines readable.
- Put imports at the top of files.
- Use comments to explain why, not only what.

## Python Memory Management Basics

Python automatically manages memory for you. When you create a value, Python stores it in memory. When your program no longer needs it, Python's garbage collector can clean it up. Beginners do not need to manually allocate or free memory, but they should avoid creating huge unnecessary lists.

## Useful Resources

- Python official documentation: <https://docs.python.org/3/>
- Python beginner tutorial: <https://docs.python.org/3/tutorial/>
- PEP8 style guide: <https://peps.python.org/pep-0008/>
- NumPy documentation: <https://numpy.org/doc/>
- pandas documentation: <https://pandas.pydata.org/docs/>

## Final Advice

Do not rush. Run each file, change a value, predict the output, and run it again. That habit builds real programming skill.
