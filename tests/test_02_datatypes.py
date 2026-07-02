"""Tests for Chapter 02: Data Types."""

import pytest


class TestNumbers:
    """Test integer and float types."""

    def test_integer_creation(self):
        """Test creating and using integers."""
        age = 16
        assert isinstance(age, int)
        assert age == 16

    def test_float_creation(self):
        """Test creating and using floats."""
        average_marks = 87.5
        assert isinstance(average_marks, float)
        assert average_marks == 87.5

    def test_integer_arithmetic(self):
        """Test arithmetic operations on integers."""
        a = 10
        b = 3
        assert a + b == 13
        assert a - b == 7
        assert a * b == 30
        assert a // b == 3

    def test_float_arithmetic(self):
        """Test arithmetic operations on floats."""
        a = 10.5
        b = 2.5
        assert a + b == 13.0
        assert a - b == 8.0
        assert a * b == 26.25

    def test_mixed_arithmetic(self):
        """Test arithmetic with mixed int and float."""
        result = 10 + 5.5
        assert isinstance(result, float)
        assert result == 15.5


class TestStrings:
    """Test string type and operations."""

    def test_string_creation_double_quotes(self):
        """Test creating strings with double quotes."""
        name = "Alex"
        assert name == "Alex"
        assert isinstance(name, str)

    def test_string_creation_single_quotes(self):
        """Test creating strings with single quotes."""
        message = 'Welcome to Python!'
        assert message == "Welcome to Python!"

    def test_string_concatenation(self):
        """Test string concatenation."""
        greeting = "Hello, " + "World!"
        assert greeting == "Hello, World!"

    def test_string_multiplication(self):
        """Test string repetition."""
        repeated = "ab" * 3
        assert repeated == "ababab"

    def test_string_indexing(self):
        """Test accessing individual characters."""
        text = "Python"
        assert text[0] == "P"
        assert text[-1] == "n"

    def test_string_slicing(self):
        """Test string slicing."""
        text = "Python"
        assert text[1:4] == "yth"
        assert text[:3] == "Pyt"

    def test_string_length(self):
        """Test len() function on strings."""
        text = "Hello"
        assert len(text) == 5

    def test_string_methods(self):
        """Test common string methods."""
        text = "  hello world  "
        assert text.strip() == "hello world"
        assert text.upper() == "  HELLO WORLD  "
        assert text.lower() == text


class TestBooleans:
    """Test boolean type and logic."""

    def test_boolean_true(self):
        """Test True value."""
        assert True is True
        assert isinstance(True, bool)

    def test_boolean_false(self):
        """Test False value."""
        assert False is False
        assert isinstance(False, bool)

    def test_boolean_from_comparison(self):
        """Test creating boolean from comparison."""
        result = 5 > 3
        assert result is True
        result = 5 < 3
        assert result is False

    def test_boolean_from_expression(self):
        """Test boolean in conditional expressions."""
        marks = 85
        passed = marks >= 40
        assert passed is True


class TestTypeConversion:
    """Test type conversion functions."""

    def test_int_conversion(self):
        """Test converting to integer."""
        text_number = "10"
        real_total = int(text_number) + 5
        assert real_total == 15
        assert isinstance(real_total, int)

    def test_float_conversion(self):
        """Test converting to float."""
        text_float = "3.14"
        value = float(text_float)
        assert value == 3.14
        assert isinstance(value, float)

    def test_str_conversion(self):
        """Test converting to string."""
        number = 42
        text = str(number)
        assert text == "42"
        assert isinstance(text, str)

    def test_int_conversion_from_float(self):
        """Test converting float to int (truncates)."""
        value = int(3.99)
        assert value == 3

    def test_bool_conversion(self):
        """Test converting to boolean."""
        assert bool(1) is True
        assert bool(0) is False
        assert bool("text") is True
        assert bool("") is False


class TestInputOutput:
    """Test print function and output."""

    def test_print_single_value(self, capture_output):
        """Test printing a single value."""
        print("Hello, World!")
        output = capture_output.getvalue()
        assert "Hello, World!" in output

    def test_print_multiple_values(self, capture_output):
        """Test printing multiple values."""
        print("Name:", "Alice")
        output = capture_output.getvalue()
        assert "Name:" in output
        assert "Alice" in output

    def test_print_formatted_string(self, capture_output):
        """Test f-string formatting."""
        name = "Maya"
        age = 16
        print(f"Hello, {name}! You are {age} years old.")
        output = capture_output.getvalue()
        assert "Hello, Maya!" in output
        assert "16" in output
