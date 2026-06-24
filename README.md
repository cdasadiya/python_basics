# 🐍 Python Basic Tutorial

<div align="center">

**A beginner-friendly Python learning path from first program to practical intermediate concepts.**

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Level](https://img.shields.io/badge/Level-Beginner%20Friendly-success)](#-learning-path)
[![Topics](https://img.shields.io/badge/Chapters-22-orange)](#-repository-structure)

</div>

---

## 👋 Welcome

This repository teaches Python in simple English for learners who are new to programming. Each topic lives in its own file, so you can read, run, experiment, and understand one concept at a time.

Think of programming like writing a recipe for a computer: you give clear step-by-step instructions, and Python helps the computer calculate, decide, repeat, store, and display information.

## ✨ Why Learners Like This Course

- 📚 **Chapter-wise flow** from absolute basics to intermediate topics
- 🧩 **One concept per file** for focused learning
- ▶️ **Independent examples** that can be run directly
- 💬 **Beginner-friendly comments** inside the code
- ✅ **Expected outputs** shown in file headers
- 🧠 **Common mistakes, best practices, and interview questions** included
- 🛠️ **Practical libraries** such as `requests`, `numpy`, and `pandas`
- 🧪 **Easy verification** with Python's built-in compile check

## 👤 Author

| Field | Details |
|---|---|
| Author | Chaitanya Dasadiya |
| LinkedIn | <https://www.linkedin.com/in/chaitanya-dasadiya> |

> **Privacy note:** This README intentionally does not publish a personal email address. Please use the LinkedIn profile above for professional contact.

## 🚀 Quick Start

### 1. Install Python

Install **Python 3.13 or newer** from <https://www.python.org/downloads/>.

Check your version:

```bash
python --version
```

### 2. Clone or Download This Repository

If you use Git:

```bash
git clone <repository-url>
cd python_basics
```

If you downloaded a ZIP file, extract it and open the extracted folder in your terminal.

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Required Packages

```bash
python -m pip install -r requirements.txt
```

### 5. Run Your First Program

```bash
python 01_introduction/03_first_program.py
```

Try another example:

```bash
python 05_loops/01_for_loop.py
```

## 🧭 Learning Path

| Step | Chapter | What You Learn |
|---:|---|---|
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
├── AUDIT_REPORT.md
├── README.md
└── requirements.txt
```

## 🧪 Verify Everything Works

Compile every Python file:

```bash
python -m compileall -q .
```

This checks that all Python files have valid syntax. You can also run topic files one by one for hands-on practice.

## 🧰 Requirements

Third-party examples use:

- `requests`
- `numpy`
- `pandas`

Install them with:

```bash
python -m pip install -r requirements.txt
```

## 🐍 Python vs Other Languages

| Feature | Python | Java | C++ | JavaScript |
|---|---|---|---|---|
| Beginner friendly | Very high | Medium | Lower | Medium |
| Syntax | Simple | Verbose | Complex | Flexible |
| Main uses | Data, web, automation, AI | Enterprise apps | Systems, games | Web browsers and servers |
| Speed | Good for most tasks | Fast | Very fast | Fast |

## 📈 Audit and Expansion Roadmap

A detailed repository audit and professional expansion plan is available in [`AUDIT_REPORT.md`](AUDIT_REPORT.md). It reviews the current learning structure, highlights duplicate or missing topics, and proposes a roadmap for growing this repository into a stronger Python and AI-foundations course.

## 💡 Tips for Learners

- Start from chapter 1 and move in order.
- Read comments before running a file.
- Change values and run again to see what happens.
- Do not fear errors; debugging is an important programming skill.
- Take notes after every chapter.
- Revisit examples after a few days to strengthen memory.

## ⭐ Suggested Study Routine

| Day | Goal |
|---:|---|
| 1 | Run the introduction and datatype examples |
| 2 | Practice operators and conditions |
| 3 | Learn loops and range |
| 4 | Explore lists, tuples, dictionaries, and sets |
| 5 | Practice functions and strings |
| 6 | Try file handling, modules, and date/time |
| 7 | Review assignments and start NumPy/pandas basics |

---

<div align="center">

**Happy learning and keep practicing! 🚀**

</div>
