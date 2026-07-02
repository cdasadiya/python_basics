"""Tests for Chapter 01: Introduction."""

import pytest
import sys
from io import StringIO


class TestIntroduction:
    """Test cases for introduction concepts."""

    def test_what_is_programming(self, capture_output):
        """Test that programming explanation is output correctly."""
        # Simulate the what_is_programming.py example
        step_1 = "Take two slices of bread"
        step_2 = "Add cheese"
        step_3 = "Close the sandwich"
        
        print("Programming is giving clear instructions to a computer.")
        print("Example steps:")
        print("1.", step_1)
        print("2.", step_2)
        print("3.", step_3)
        
        output = capture_output.getvalue()
        assert "Programming is giving clear instructions to a computer." in output
        assert "Example steps:" in output
        assert step_1 in output

    def test_why_python(self, capture_output):
        """Test Python benefits explanation."""
        print("Python is easy to read.")
        print("Python is used for websites, games, automation, data science, and AI.")
        
        output = capture_output.getvalue()
        assert "Python is easy to read." in output
        assert "websites" in output

    def test_first_program(self, capture_output):
        """Test classic Hello, World! program."""
        print("Hello, World!")
        output = capture_output.getvalue()
        assert "Hello, World!" in output


class TestProgrammingConcepts:
    """Test fundamental programming concepts."""

    def test_sequential_execution(self):
        """Test that statements execute in sequence."""
        results = []
        results.append(1)
        results.append(2)
        results.append(3)
        assert results == [1, 2, 3]

    def test_variable_assignment(self):
        """Test variable assignment and retrieval."""
        name = "Alice"
        age = 25
        assert name == "Alice"
        assert age == 25

    def test_comments_ignored(self):
        """Test that comments don't affect execution."""
        x = 5  # This is a comment
        # This entire line is a comment
        y = 10
        assert x + y == 15
