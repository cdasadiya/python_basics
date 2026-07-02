"""Tests for Chapter 03: Operators."""

import pytest


class TestArithmeticOperators:
    """Test arithmetic operations."""

    def test_addition(self):
        """Test addition operator."""
        assert 10 + 3 == 13
        assert 5.5 + 2.5 == 8.0

    def test_subtraction(self):
        """Test subtraction operator."""
        assert 10 - 3 == 7
        assert 5.5 - 2.5 == 3.0

    def test_multiplication(self):
        """Test multiplication operator."""
        assert 10 * 3 == 30
        assert 5.5 * 2 == 11.0

    def test_division(self):
        """Test division operator."""
        assert 10 / 2 == 5.0
        assert 10 / 4 == 2.5

    def test_floor_division(self):
        """Test floor division operator."""
        assert 10 // 3 == 3
        assert 10 // 4 == 2

    def test_modulo(self):
        """Test modulo operator."""
        assert 10 % 3 == 1
        assert 10 % 2 == 0

    def test_power(self):
        """Test power operator."""
        assert 10 ** 2 == 100
        assert 2 ** 3 == 8

    def test_operator_precedence(self):
        """Test operator precedence."""
        assert 2 + 3 * 4 == 14  # Multiplication before addition
        assert (2 + 3) * 4 == 20  # Parentheses change order


class TestComparisonOperators:
    """Test comparison operations."""

    def test_greater_than(self):
        """Test > operator."""
        assert 10 > 3 is True
        assert 3 > 10 is False

    def test_less_than(self):
        """Test < operator."""
        assert 3 < 10 is True
        assert 10 < 3 is False

    def test_greater_equal(self):
        """Test >= operator."""
        assert 10 >= 10 is True
        assert 10 >= 5 is True

    def test_less_equal(self):
        """Test <= operator."""
        assert 10 <= 10 is True
        assert 5 <= 10 is True

    def test_equal(self):
        """Test == operator."""
        assert 10 == 10 is True
        assert 10 == 5 is False

    def test_not_equal(self):
        """Test != operator."""
        assert 10 != 5 is True
        assert 10 != 10 is False


class TestLogicalOperators:
    """Test logical operations."""

    def test_and_operator(self):
        """Test 'and' operator."""
        assert (True and True) is True
        assert (True and False) is False
        assert (False and False) is False

    def test_or_operator(self):
        """Test 'or' operator."""
        assert (True or False) is True
        assert (False or False) is False
        assert (True or True) is True

    def test_not_operator(self):
        """Test 'not' operator."""
        assert (not True) is False
        assert (not False) is True

    def test_complex_logical_expression(self):
        """Test complex logical expressions."""
        age = 16
        has_ticket = True
        can_enter = age >= 13 and has_ticket
        assert can_enter is True


class TestMembershipOperators:
    """Test membership operations."""

    def test_in_operator(self):
        """Test 'in' operator."""
        fruits = ["apple", "banana", "orange"]
        assert "banana" in fruits
        assert "grape" not in fruits

    def test_not_in_operator(self):
        """Test 'not in' operator."""
        text = "Python"
        assert "y" in text
        assert "z" not in text

    def test_membership_with_strings(self):
        """Test membership with string checking."""
        assert "p" in "Python"
        assert "P" in "Python"
        assert "x" not in "Python"


class TestIdentityOperators:
    """Test identity operations."""

    def test_is_operator_same_object(self):
        """Test 'is' operator with same object reference."""
        first = [1, 2, 3]
        second = first
        assert first is second

    def test_is_operator_different_objects(self):
        """Test 'is' operator with different objects."""
        first = [1, 2, 3]
        third = [1, 2, 3]
        assert first is not third

    def test_equal_vs_identity(self):
        """Test == (value) vs is (identity)."""
        first = [1, 2, 3]
        third = [1, 2, 3]
        assert first == third  # Same value
        assert first is not third  # Different objects


class TestBitwiseOperators:
    """Test bitwise operations."""

    def test_bitwise_and(self):
        """Test bitwise AND operator."""
        # 5 = 0101, 6 = 0110, AND = 0100 = 4
        assert (5 & 6) == 4

    def test_bitwise_or(self):
        """Test bitwise OR operator."""
        # 5 = 0101, 6 = 0110, OR = 0111 = 7
        assert (5 | 6) == 7

    def test_bitwise_xor(self):
        """Test bitwise XOR operator."""
        # 5 = 0101, 6 = 0110, XOR = 0011 = 3
        assert (5 ^ 6) == 3


class TestAssignmentOperators:
    """Test assignment operations."""

    def test_simple_assignment(self):
        """Test basic assignment."""
        x = 10
        assert x == 10

    def test_add_assign(self):
        """Test += operator."""
        x = 10
        x += 5
        assert x == 15

    def test_subtract_assign(self):
        """Test -= operator."""
        x = 10
        x -= 3
        assert x == 7

    def test_multiply_assign(self):
        """Test *= operator."""
        x = 10
        x *= 2
        assert x == 20

    def test_divide_assign(self):
        """Test /= operator."""
        x = 10
        x /= 2
        assert x == 5.0
