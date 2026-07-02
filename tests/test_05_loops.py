"""Tests for Chapter 05: Loops."""

import pytest


class TestForLoop:
    """Test for loops."""

    def test_for_loop_over_list(self):
        """Test iterating over a list."""
        languages = ["Python", "Java", "C++"]
        result = []
        for language in languages:
            result.append(language)
        assert result == ["Python", "Java", "C++"]

    def test_for_loop_over_range(self):
        """Test iterating over a range."""
        result = []
        for i in range(1, 4):
            result.append(i)
        assert result == [1, 2, 3]

    def test_for_loop_over_string(self):
        """Test iterating over a string."""
        result = []
        for char in "abc":
            result.append(char)
        assert result == ["a", "b", "c"]

    def test_for_loop_enumerate(self):
        """Test enumerate in for loop."""
        items = ["a", "b", "c"]
        result = []
        for index, item in enumerate(items):
            result.append((index, item))
        assert result == [(0, "a"), (1, "b"), (2, "c")]


class TestWhileLoop:
    """Test while loops."""

    def test_while_loop_basic(self):
        """Test basic while loop."""
        count = 1
        result = []
        while count <= 3:
            result.append(count)
            count += 1
        assert result == [1, 2, 3]

    def test_while_loop_false_condition(self):
        """Test while loop with false condition."""
        count = 5
        result = []
        while count < 3:
            result.append(count)
            count += 1
        assert result == []

    def test_while_loop_infinite_prevention(self):
        """Test while loop with counter."""
        count = 0
        iterations = 0
        while count < 3:
            iterations += 1
            count += 1
        assert iterations == 3


class TestBreakStatement:
    """Test break statement."""

    def test_break_in_for_loop(self):
        """Test break exits for loop."""
        result = []
        for number in range(1, 6):
            if number == 3:
                break
            result.append(number)
        assert result == [1, 2]

    def test_break_in_while_loop(self):
        """Test break exits while loop."""
        count = 1
        result = []
        while True:
            if count > 3:
                break
            result.append(count)
            count += 1
        assert result == [1, 2, 3]


class TestContinueStatement:
    """Test continue statement."""

    def test_continue_in_for_loop(self):
        """Test continue skips iteration."""
        result = []
        for number in range(1, 6):
            if number % 2 == 0:
                continue
            result.append(number)
        assert result == [1, 3, 5]

    def test_continue_in_while_loop(self):
        """Test continue in while loop."""
        count = 0
        result = []
        while count < 5:
            count += 1
            if count % 2 == 0:
                continue
            result.append(count)
        assert result == [1, 3, 5]


class TestPassStatement:
    """Test pass statement."""

    def test_pass_in_if(self):
        """Test pass as placeholder in if."""
        x = 5
        if x > 0:
            pass  # Placeholder for future code
        assert x == 5

    def test_pass_in_loop(self):
        """Test pass as placeholder in loop."""
        result = 0
        for i in range(3):
            pass  # Placeholder
            result += 1
        assert result == 3


class TestNestedLoops:
    """Test nested loops."""

    def test_nested_for_loops(self):
        """Test nested for loops."""
        result = []
        for i in range(1, 3):
            for j in range(1, 3):
                result.append((i, j))
        assert result == [(1, 1), (1, 2), (2, 1), (2, 2)]

    def test_nested_with_break(self):
        """Test nested loop with break."""
        result = []
        for i in range(1, 4):
            for j in range(1, 4):
                if j == 2:
                    break
                result.append((i, j))
        assert result == [(1, 1), (2, 1), (3, 1)]


class TestLoopControls:
    """Test loop control flow."""

    def test_else_after_for_loop(self):
        """Test else clause after for loop."""
        executed_else = False
        for i in range(3):
            pass
        else:
            executed_else = True
        assert executed_else is True

    def test_else_not_executed_with_break(self):
        """Test else not executed when break occurs."""
        executed_else = False
        for i in range(3):
            if i == 1:
                break
        else:
            executed_else = True
        assert executed_else is False
