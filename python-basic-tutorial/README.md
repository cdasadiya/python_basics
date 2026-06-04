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
└── requirements.txt
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

## Verify the Repository

After installing dependencies, you can check that all example files compile:

```bash
python -m compileall -q .
```

You can also run individual examples one at a time. Third-party examples in the NumPy, pandas, and requests chapters include beginner-safe dependency messages if a package is missing.

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
14. Extra professional topics: comments, variables, constants, escape characters, PEP8, memory basics, virtual environments, pip, and requirements files

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
