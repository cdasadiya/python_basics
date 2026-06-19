# Python Basic Tutorial

A complete beginner-friendly Python learning repository from absolute beginner to intermediate level.

## Author

| Field | Details |
|---|---|
| Author | Chaitanya Dasadiya |
| LinkedIn | <https://www.linkedin.com/in/chaitanya-dasadiya> |

## About This Repository

This repository is designed for a 16-year-old student with no programming background. Every topic is explained in simple English and placed in its own Python file so learners can run one concept at a time.

### What makes this course beginner friendly?

- Chapter-wise structure from basics to intermediate topics
- One topic per file
- Every Python file runs independently
- Detailed comments inside examples
- Expected output shown in each file header
- Common mistakes, interview questions, and best practices included
- No large projects; only focused topic-based programs
- Third-party examples include helpful install messages if packages are missing

## What Is Programming?

Programming means writing step-by-step instructions that a computer can follow. A recipe tells a person how to cook; a program tells a computer how to calculate, decide, repeat, store, and display information.

## Why Python?

Python is popular because it is readable, beginner friendly, and powerful. It is used in web development, automation, data science, artificial intelligence, scripting, testing, and education.

## Installation Guide

1. Install Python 3.13 or newer from <https://www.python.org/downloads/>.
2. Check Python version:

   ```bash
   python --version
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment:

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

## How to Run Programs

Run any file from the repository root:

```bash
python 01_introduction/03_first_program.py
```

Run another example:

```bash
python 05_loops/01_for_loop.py
```

For NumPy, pandas, and requests chapters, install dependencies first:

```bash
python -m pip install -r requirements.txt
```

## Verify the Repository

Compile every Python file:

```bash
python -m compileall -q .
```

Run all topic files one by one if you want a full local check. Third-party examples include beginner-safe dependency messages if a package is missing.

## Learning Path

| Step | Chapter | What You Learn |
|---|---|---|
| 1 | Introduction | Programming, Python, first program |
| 2 | Datatypes | Numbers, strings, booleans, conversion, input/output |
| 3 | Operators | Arithmetic, comparison, assignment, logical, membership, identity, bitwise |
| 4 | Conditions | `if`, `if else`, `elif`, nested decisions, marks example |
| 5 | Loops | `for`, `while`, `break`, `continue`, `pass`, nested loops |
| 6 | Range | `range()`, examples, Python 2 `xrange` comparison |
| 7 | Python 2 vs Python 3 | Print, input, division, Unicode, summary |
| 8 | Lists | List methods, slicing, nested lists, comprehensions |
| 9 | Exercise | Todo-list style list practice |
| 10 | Functions | Parameters, return, defaults, scope, nested functions, lambda, recursion |
| 11 | Strings | Creation, quotes, indexing, slicing, methods, f-strings |
| 12 | Error Handling | Built-in errors, `try except`, `finally`, custom exceptions |
| 13 | File Handling | Text and CSV read/write/append |
| 14 | Dictionary | Create, access, update, keys, values, loops, nesting |
| 15 | Tuple | Creation, access, operations, unpacking, list vs tuple |
| 16 | Sets | Unique values and set operations |
| 17 | Modules | `math`, `random`, `os`, `json`, `requests` |
| 18 | Date & Time | `datetime`, `date`, `time`, `timedelta`, age calculator |
| 19 | Assignments | Duplicates, frequency counts, removing duplicates |
| 20 | NumPy | Arrays, indexing, slicing, shape, reshape, broadcasting, math |
| 21 | pandas | Series, DataFrame, CSV, filtering, groupby, analysis |
| 22 | Extra Topics | Comments, type casting, `enumerate`, `zip`, PEP8, memory, pip, venv |

## Repository Structure

```text
./
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
├── 22_extra_topics/
├── README.md
└── requirements.txt
```

## Python vs Other Languages

| Feature | Python | Java | C++ | JavaScript |
|---|---|---|---|---|
| Beginner friendly | Very high | Medium | Lower | Medium |
| Syntax | Simple | Verbose | Complex | Flexible |
| Main uses | Data, web, automation, AI | Enterprise apps | Systems, games | Web browsers and servers |
| Speed | Good for most tasks | Fast | Very fast | Fast |

## Requirements

Third-party examples use these packages:

- `requests`
- `numpy`
- `pandas`

Install them with:

```bash
python -m pip install -r requirements.txt
```

## Notes for Learners

- Start from chapter 1 and move in order.
- Read the comments before running each file.
- Change values and run again to understand behavior.
- Do not skip mistakes; debugging is part of learning.
