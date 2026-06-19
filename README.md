# 🐍 Python Basic Tutorial

> A polished, beginner-friendly Python learning path that takes students from **zero programming knowledge** to confident intermediate-level Python practice.

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.13%2B-blue?logo=python&logoColor=white">
  <img alt="Level" src="https://img.shields.io/badge/Level-Beginner%20to%20Intermediate-brightgreen">
  <img alt="Learning Style" src="https://img.shields.io/badge/Style-One%20topic%20per%20file-orange">
</p>

---

## 👤 Author

| Field | Details |
|---|---|
| Author | Chaitanya Dasadiya |
| LinkedIn | <https://www.linkedin.com/in/chaitanya-dasadiya> |

> **Privacy note:** This README intentionally does not publish a personal email address. Please use the LinkedIn profile above for professional contact.

---

## 📌 About This Repository

This repository is designed for learners who are new to programming, including young students starting from scratch. Each topic is explained with simple examples, practical comments, expected output, common mistakes, interview questions, and best practices.

### ✨ Why this course is beginner friendly

- 📚 **Chapter-wise learning path** from basics to intermediate topics
- 🧩 **One topic per file** so each concept stays focused
- ▶️ **Runnable examples** that can be executed independently
- 💬 **Detailed comments** written in simple English
- ✅ **Expected output** included in file headers
- ⚠️ **Common mistakes** listed to help learners debug faster
- 🎯 **Interview-style questions** for revision and confidence building
- 🛡️ **Safe third-party examples** with helpful dependency messages

---

## 🧠 What Is Programming?

Programming means writing step-by-step instructions that a computer can follow. Think of it like a recipe: a recipe tells a person how to cook, while a program tells a computer how to calculate, decide, repeat, store, and display information.

---

## 🚀 Why Python?

Python is one of the best first programming languages because it is readable, practical, and widely used. It is popular in:

- 🌐 Web development
- 🤖 Automation and scripting
- 📊 Data analysis
- 🧪 Testing
- 🧠 Artificial intelligence and machine learning
- 🎓 Education and beginner programming

---

## 🛠️ Installation Guide

### 1. Install Python

Install **Python 3.13 or newer** from the official website:

<https://www.python.org/downloads/>

Check your installed version:

```bash
python --version
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ How to Run Programs

Run examples from the repository root.

```bash
python 01_introduction/03_first_program.py
```

Try another file:

```bash
python 05_loops/01_for_loop.py
```

> NumPy, pandas, and requests examples require dependencies from `requirements.txt`.

---

## ✅ Verify the Repository

Compile every Python file to confirm syntax correctness:

```bash
python -m compileall -q .
```

You can also run chapter files one by one while learning. Third-party examples show beginner-safe install guidance if a package is missing.

---

## 🗺️ Learning Path

| Step | Chapter | What You Learn |
|---:|---|---|
| 1 | `01_introduction` | Programming basics, why Python, first program |
| 2 | `02_datatypes` | Numbers, strings, booleans, conversion, input/output |
| 3 | `03_operators` | Arithmetic, comparison, assignment, logical, membership, identity, bitwise |
| 4 | `04_conditions` | `if`, `if else`, `elif`, nested decisions, marks example |
| 5 | `05_loops` | `for`, `while`, `break`, `continue`, `pass`, nested loops |
| 6 | `06_range` | `range()`, examples, Python 2 `xrange` comparison |
| 7 | `07_python2_vs_python3` | Print, input, division, Unicode, summary |
| 8 | `08_lists` | List methods, slicing, nested lists, comprehensions |
| 9 | `09_exercise` | Todo-list style list practice |
| 10 | `10_functions` | Parameters, return values, defaults, scope, nested functions, lambda, recursion |
| 11 | `11_strings` | Creation, quotes, indexing, slicing, methods, f-strings |
| 12 | `12_error_handling` | Built-in errors, `try except`, `finally`, custom exceptions |
| 13 | `13_file_handling` | Text files and CSV read/write/append |
| 14 | `14_dictionary` | Create, access, update, keys, values, loops, nesting |
| 15 | `15_tuple` | Creation, access, operations, unpacking, list vs tuple |
| 16 | `16_sets` | Unique values and set operations |
| 17 | `17_modules` | `math`, `random`, `os`, `json`, `requests` |
| 18 | `18_datetime` | `datetime`, `date`, `time`, `timedelta`, age calculator |
| 19 | `19_assignments` | Duplicates, frequency counts, removing duplicates |
| 20 | `20_numpy` | Arrays, indexing, slicing, shape, reshape, broadcasting, math |
| 21 | `21_pandas` | Series, DataFrame, CSV, filtering, groupby, analysis |
| 22 | `22_extra_topics` | Comments, type casting, `enumerate`, `zip`, PEP8, memory, pip, venv |

---

## 🗂️ Repository Structure

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

---

## 🧾 Requirements

The core Python examples use the standard library. A few later chapters use third-party packages:

| Package | Used For |
|---|---|
| `requests` | Preparing HTTP/API request examples |
| `numpy` | Numerical arrays and vectorized operations |
| `pandas` | DataFrame, CSV, filtering, grouping, and analysis examples |

Install all dependencies with:

```bash
python -m pip install -r requirements.txt
```

---

## 🆚 Python vs Other Languages

| Feature | Python | Java | C++ | JavaScript |
|---|---|---|---|---|
| Beginner friendly | Very high | Medium | Lower | Medium |
| Syntax style | Simple and readable | Verbose | Complex | Flexible |
| Common uses | Data, web, automation, AI | Enterprise apps | Systems, games | Web apps and servers |
| Speed | Good for most learning and scripting tasks | Fast | Very fast | Fast |

---

## 🎯 Suggested Study Routine

1. Start with `01_introduction` and move in order.
2. Read the comments before running each file.
3. Run the file and compare the output with the expected output.
4. Change values and run again to understand behavior.
5. Write your own small example after every topic.
6. Revisit common mistakes and interview questions for revision.

---

## 🤝 Contribution Notes

If you improve examples or add new topics, keep the repository beginner friendly:

- Use clear file names.
- Keep one main concept per file.
- Add comments that explain the “why,” not only the “what.”
- Avoid exposing private contact details such as real email addresses.
- Prefer safe examples that do not require external services unless clearly documented.

---

## 🌟 Final Note

Learning programming is a step-by-step journey. Run the examples, make mistakes, debug them, and keep practicing consistently.
