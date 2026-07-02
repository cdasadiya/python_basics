"""Tests for Chapter 04: Conditions."""

import pytest


class TestIfStatement:
    """Test if statement."""

    def test_if_true_condition(self):
        """Test if with true condition."""
        age = 16
        result = None
        if age >= 13:
            result = "Can watch"
        assert result == "Can watch"

    def test_if_false_condition(self):
        """Test if with false condition."""
        age = 10
        result = None
        if age >= 13:
            result = "Can watch"
        assert result is None


class TestIfElseStatement:
    """Test if-else statement."""

    def test_if_else_true_branch(self):
        """Test if-else taking if branch."""
        marks = 72
        result = None
        if marks >= 40:
            result = "Passed"
        else:
            result = "Failed"
        assert result == "Passed"

    def test_if_else_false_branch(self):
        """Test if-else taking else branch."""
        marks = 30
        result = None
        if marks >= 40:
            result = "Passed"
        else:
            result = "Failed"
        assert result == "Failed"


class TestIfElifElseStatement:
    """Test if-elif-else statement."""

    def test_elif_first_condition(self):
        """Test if condition matches."""
        marks = 91
        grade = None
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        else:
            grade = "C"
        assert grade == "A"

    def test_elif_second_condition(self):
        """Test elif condition matches."""
        marks = 80
        grade = None
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        else:
            grade = "C"
        assert grade == "B"

    def test_elif_else_branch(self):
        """Test else branch matches."""
        marks = 60
        grade = None
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        else:
            grade = "C"
        assert grade == "C"


class TestNestedConditions:
    """Test nested if statements."""

    def test_nested_if(self):
        """Test nested if statements."""
        marks = 91
        grade = None
        comment = None
        if marks >= 90:
            grade = "A"
            if marks >= 95:
                comment = "Outstanding"
            else:
                comment = "Excellent"
        assert grade == "A"
        assert comment == "Excellent"

    def test_nested_if_outer_false(self):
        """Test nested if when outer is false."""
        marks = 80
        grade = None
        comment = None
        if marks >= 90:
            grade = "A"
            if marks >= 95:
                comment = "Outstanding"
            else:
                comment = "Excellent"
        else:
            grade = "B"
        assert grade == "B"
        assert comment is None


class TestRealWorldExamples:
    """Test real-world conditional examples."""

    def test_pass_fail_grade_logic(self):
        """Test complete pass/fail and grading logic."""
        marks = 82
        
        # Pass/Fail
        result = "Pass" if marks >= 40 else "Fail"
        assert result == "Pass"
        
        # Grade
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        else:
            grade = "C"
        assert grade == "B"

    def test_age_based_access(self):
        """Test age-based access control."""
        age = 25
        has_permission = age >= 18
        assert has_permission is True

    def test_multiple_conditions(self):
        """Test multiple conditions combined."""
        age = 16
        has_ticket = True
        can_enter = age >= 13 and has_ticket
        assert can_enter is True


class TestTruthyFalsy:
    """Test truthy and falsy values."""

    def test_truthy_values(self):
        """Test values that evaluate to True."""
        assert bool(1) is True
        assert bool("text") is True
        assert bool([1, 2]) is True
        assert bool({"key": "value"}) is True

    def test_falsy_values(self):
        """Test values that evaluate to False."""
        assert bool(0) is False
        assert bool("") is False
        assert bool([]) is False
        assert bool({}) is False
        assert bool(None) is False
