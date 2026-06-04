# Python Basic Tutorial

<p align="center">
  <strong>A complete beginner-friendly Python learning repository from absolute beginner to intermediate level.</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white">
  <img alt="Level" src="https://img.shields.io/badge/Level-Beginner%20to%20Intermediate-brightgreen">
  <img alt="Style" src="https://img.shields.io/badge/Style-Topic%20Based-blue">
  <img alt="License" src="https://img.shields.io/badge/Use-Educational-orange">
</p>

---

## 👨‍🏫 Author

| Field | Details |
|---|---|
| **Author** | **Chaitanya Dasadiya** |
| **LinkedIn** | <https://www.linkedin.com/in/chaitanya-dasadiya> |

---

## 📌 About This Repository

This repository is designed for a **16-year-old student with no programming background**. Every topic is explained in simple English and placed in its own Python file so learners can run one concept at a time.

### What makes this course beginner friendly?

- ✅ Chapter-wise structure from basics to intermediate topics
- ✅ One topic per file
- ✅ Every Python file runs independently
- ✅ Detailed comments inside examples
- ✅ Expected output shown in each file header
- ✅ Common mistakes, interview questions, and best practices included
- ✅ No large projects; only focused topic-based programs
- ✅ Third-party examples include helpful install messages if packages are missing

---

## 🧠 What Is Programming?

Programming means writing step-by-step instructions that a computer can follow. A recipe tells a person how to cook; a program tells a computer how to calculate, decide, repeat, store, and display information.

---

## 🐍 Why Python?

Python is popular because it is readable, beginner friendly, and powerful. It is used in:

- Web development
- Automation
- Data science
- Artificial intelligence
- Scripting
- Testing
- Education

---

## ⚙️ Installation Guide

### 1. Install Python

Install **Python 3.13 or newer** from the official website:

<https://www.python.org/downloads/>

### 2. Check Python version

```bash
python --version
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install required packages

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ How to Run Programs

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

---

## ✅ Verify the Repository

Compile every Python file:

```bash
python -m compileall -q .
```

Run all topic files one by one if you want a full local check. Third-party examples include beginner-safe dependency messages if a package is missing.

---

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

---

## 📁 Repository Structure

```text
./
├── 01_introduction/
│   ├── 01_what_is_programming.py
│   ├── 02_why_python.py
│   └── 03_first_program.py
├── 02_datatypes/
│   ├── 01_numbers.py
│   ├── 02_strings.py
│   ├── 03_boolean.py
│   ├── 04_type_conversion.py
│   └── 05_input_output.py
├── 03_operators/
│   ├── 01_arithmetic.py
│   ├── 02_comparison.py
│   ├── 03_assignment.py
│   ├── 04_logical.py
│   ├── 05_membership.py
│   ├── 06_identity.py
│   └── 07_bitwise.py
├── 04_conditions/
│   ├── 01_if.py
│   ├── 02_if_else.py
│   ├── 03_if_elif_else.py
│   └── 04_marks_example.py
├── 05_loops/
│   ├── 01_for_loop.py
│   ├── 02_while_loop.py
│   ├── 03_break.py
│   ├── 04_continue.py
│   ├── 05_pass.py
│   └── 06_nested_loop.py
├── 06_range/
│   ├── 01_range.py
│   ├── 02_range_examples.py
│   └── 03_range_vs_xrange.py
├── 07_python2_vs_python3/
│   ├── 01_print_statement.py
│   ├── 02_xrange.py
│   ├── 03_raw_input.py
│   ├── 04_integer_division.py
│   ├── 05_unicode.py
│   └── 06_summary.py
├── 08_lists/
│   ├── 01_create_list.py
│   ├── 02_append.py
│   ├── 03_extend.py
│   ├── 04_insert.py
│   ├── 05_remove.py
│   ├── 06_pop.py
│   ├── 07_clear.py
│   ├── 08_sort.py
│   ├── 09_reverse.py
│   ├── 10_copy.py
│   ├── 11_count.py
│   ├── 12_index.py
│   ├── 13_list_slicing.py
│   ├── 14_nested_list.py
│   ├── 15_list_comprehension.py
│   └── 16_real_time_examples.py
├── 09_exercise/
│   └── todo_list_using_lists.py
├── 10_functions/
│   ├── 01_basic_function.py
│   ├── 02_parameter_function.py
│   ├── 03_return_function.py
│   ├── 04_default_parameter.py
│   ├── 05_keyword_arguments.py
│   ├── 06_variable_arguments.py
│   ├── 07_scope_local_global.py
│   ├── 08_nested_function.py
│   ├── 09_lambda_function.py
│   └── 10_recursion.py
├── 11_strings/
│   ├── 01_string_creation.py
│   ├── 02_single_double_quotes.py
│   ├── 03_triple_quotes.py
│   ├── 04_indexing.py
│   ├── 05_slicing.py
│   ├── 06_concatenation.py
│   ├── 07_repetition.py
│   ├── 08_length.py
│   ├── 09_substring.py
│   ├── 10_upper.py
│   ├── 11_lower.py
│   ├── 12_join.py
│   ├── 13_strip.py
│   ├── 14_split.py
│   ├── 15_replace.py
│   └── 16_f_string.py
├── 12_error_handling/
│   ├── 01_try_except.py
│   ├── 02_value_error.py
│   ├── 03_syntax_error.py
│   ├── 04_type_error.py
│   ├── 05_name_error.py
│   ├── 06_zero_division_error.py
│   ├── 07_index_error.py
│   ├── 08_key_error.py
│   ├── 09_finally.py
│   └── 10_custom_exception.py
├── 13_file_handling/
│   ├── 01_write_text.py
│   ├── 02_read_text.py
│   ├── 03_append_text.py
│   ├── 04_write_csv.py
│   └── 05_read_csv.py
├── 14_dictionary/
│   ├── 01_create_dictionary.py
│   ├── 02_access_dictionary.py
│   ├── 03_update.py
│   ├── 04_clear.py
│   ├── 05_items.py
│   ├── 06_values.py
│   ├── 07_keys.py
│   ├── 08_dictionary_loop.py
│   └── 09_nested_dictionary.py
├── 15_tuple/
│   ├── 01_create_tuple.py
│   ├── 02_access_tuple.py
│   ├── 03_tuple_operations.py
│   ├── 04_unpacking.py
│   └── 05_list_vs_tuple.py
├── 16_sets/
│   ├── 01_create_set.py
│   ├── 02_unique_values.py
│   ├── 03_union.py
│   ├── 04_intersection.py
│   ├── 05_difference.py
│   └── 06_symmetric_difference.py
├── 17_modules/
│   ├── 01_math_module.py
│   ├── 02_random_module.py
│   ├── 03_os_module.py
│   ├── 04_json_module.py
│   └── 05_requests_module.py
├── 18_datetime/
│   ├── 01_datetime_now.py
│   ├── 02_date.py
│   ├── 03_time.py
│   ├── 04_timedelta.py
│   └── 05_age_calculator.py
├── 19_assignments/
│   ├── 01_find_duplicate_numbers.py
│   ├── 02_count_frequency.py
│   └── 03_remove_duplicates.py
├── 20_numpy/
│   ├── 01_create_array.py
│   ├── 02_array_access.py
│   ├── 03_array_slicing.py
│   ├── 04_array_shape.py
│   ├── 05_reshape.py
│   ├── 06_broadcasting.py
│   └── 07_numpy_math.py
├── 21_pandas/
│   ├── 01_series.py
│   ├── 02_dataframe.py
│   ├── 03_read_csv.py
│   ├── 04_write_csv.py
│   ├── 05_filter_data.py
│   ├── 06_groupby.py
│   └── 07_basic_analysis.py
├── 22_extra_topics/
│   ├── 01_comments.py
│   ├── 02_type_casting.py
│   ├── 03_enumerate.py
│   ├── 04_zip.py
│   ├── 05_list_vs_tuple_vs_set_vs_dictionary.py
│   ├── 06_virtual_environment.md
│   ├── 07_pip_installation.md
│   ├── 08_variables_and_constants.py
│   ├── 09_escape_characters.py
│   ├── 10_pep8_coding_standards.py
│   └── 11_memory_management_basics.py
├── README.md
└── requirements.txt
```

---

## 🧪 Assignments

Practice these after completing the related chapters:

1. Find duplicate numbers in a list.
2. Count the frequency of each value.
3. Remove duplicates while keeping order.
4. Modify examples by changing inputs and predicting output before running.
5. Write your own notes below each file after running it.

---

## 💬 Common Interview Questions

1. What is programming?
2. Why is Python beginner friendly?
3. What is the difference between a list and a tuple?
4. What is a dictionary and when would you use it?
5. What is the difference between `==` and `is`?
6. What is a function parameter?
7. What does `return` do?
8. What is recursion?
9. What is a custom exception?
10. What is a virtual environment?
11. Why should dependencies be stored in `requirements.txt`?
12. What is the difference between Python 2 and Python 3?

---

## 🆚 Python vs Other Languages

| Feature | Python | Java | C++ | JavaScript |
|---|---|---|---|---|
| Beginner friendly | Very high | Medium | Lower | Medium |
| Syntax | Simple | Verbose | Complex | Flexible |
| Common uses | Data, web, automation, AI | Enterprise apps | Systems, games | Web apps and servers |
| Speed | Good for most learning and business tasks | Fast | Very fast | Fast |

---

## 🔁 Python 2 vs Python 3 Summary

Use **Python 3** for all new learning and development. Python 2 is outdated.

- Python 3 uses `print()` as a function.
- Python 3 uses `input()` instead of Python 2 `raw_input()`.
- Python 3 `range()` behaves efficiently like Python 2 `xrange()`.
- Python 3 strings are Unicode by default.
- Python 3 division with `/` returns a decimal result.

---

## ✨ Python Coding Standards (PEP8)

- Use clear names like `student_marks`, not `sm`.
- Use 4 spaces for indentation.
- Keep lines readable.
- Put imports at the top of files.
- Use comments to explain why code exists.
- Keep each example focused on one topic.

---

## 🧠 Python Memory Management Basics

Python automatically manages memory for you. When you create a value, Python stores it in memory. When your program no longer needs it, Python's garbage collector can clean it up. Beginners do not need to manually allocate or free memory, but they should avoid creating huge unnecessary lists.

---

## 📦 Requirements

Third-party chapters use these packages:

- `numpy`
- `pandas`
- `requests`

Install them with:

```bash
python -m pip install -r requirements.txt
```

---

## 🔗 Useful Resources

- Python official documentation: <https://docs.python.org/3/>
- Python beginner tutorial: <https://docs.python.org/3/tutorial/>
- PEP8 style guide: <https://peps.python.org/pep-0008/>
- NumPy documentation: <https://numpy.org/doc/>
- pandas documentation: <https://pandas.pydata.org/docs/>

---

## 🌟 Final Advice

Do not rush. Run each file, change a value, predict the output, and run it again. That habit builds real programming skill.

**Happy learning and keep practicing!**
