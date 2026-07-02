"""Tests for Chapter 10: Functions."""

import pytest


class TestBasicFunctions:
    """Test basic function definitions and calls."""

    def test_function_definition_and_call(self):
        """Test defining and calling a function."""
        def greet() -> None:
            """Greet the user."""
            pass
        
        # Should not raise an error
        greet()

    def test_function_with_return(self):
        """Test function that returns a value."""
        def add_numbers(a: int, b: int) -> int:
            """Add two numbers and return result."""
            return a + b
        
        result = add_numbers(5, 3)
        assert result == 8

    def test_function_without_explicit_return(self):
        """Test function returns None if no return statement."""
        def no_return() -> None:
            """Function with no return."""
            x = 5
        
        result = no_return()
        assert result is None


class TestFunctionParameters:
    """Test function parameters and arguments."""

    def test_positional_arguments(self):
        """Test positional arguments."""
        def greet(name: str, age: int) -> str:
            return f"Hello, {name}! You are {age} years old."
        
        result = greet("Alice", 25)
        assert "Alice" in result
        assert "25" in result

    def test_keyword_arguments(self):
        """Test keyword arguments."""
        def greet(name: str, age: int) -> str:
            return f"Hello, {name}! You are {age} years old."
        
        result = greet(age=25, name="Bob")
        assert "Bob" in result
        assert "25" in result

    def test_default_parameters(self):
        """Test default parameter values."""
        def greet(name: str, greeting: str = "Hello") -> str:
            return f"{greeting}, {name}!"
        
        result1 = greet("Alice")
        assert "Hello, Alice!" == result1
        
        result2 = greet("Bob", "Hi")
        assert "Hi, Bob!" == result2

    def test_variable_length_arguments(self):
        """Test *args for variable number of arguments."""
        def sum_all(*numbers):
            return sum(numbers)
        
        assert sum_all(1, 2, 3) == 6
        assert sum_all(1, 2, 3, 4, 5) == 15

    def test_keyword_variable_arguments(self):
        """Test **kwargs for keyword arguments."""
        def print_info(**kwargs):
            return kwargs
        
        result = print_info(name="Alice", age=25)
        assert result == {"name": "Alice", "age": 25}


class TestFunctionScope:
    """Test variable scope in functions."""

    def test_local_scope(self):
        """Test local variable scope."""
        def create_var():
            x = 10
            return x
        
        result = create_var()
        assert result == 10
        assert 'x' not in dir()  # x not in global scope

    def test_global_scope(self):
        """Test global variable access."""
        global_var = 100
        
        def access_global():
            return global_var
        
        result = access_global()
        assert result == 100

    def test_variable_shadowing(self):
        """Test variable shadowing."""
        x = 5
        
        def shadow_var():
            x = 10
            return x
        
        assert shadow_var() == 10
        assert x == 5  # Original not changed


class TestLambdaFunctions:
    """Test lambda functions."""

    def test_simple_lambda(self):
        """Test simple lambda function."""
        square = lambda x: x ** 2
        assert square(5) == 25

    def test_lambda_with_multiple_args(self):
        """Test lambda with multiple arguments."""
        add = lambda x, y: x + y
        assert add(3, 4) == 7

    def test_lambda_with_map(self):
        """Test lambda with map function."""
        numbers = [1, 2, 3, 4, 5]
        squared = list(map(lambda x: x ** 2, numbers))
        assert squared == [1, 4, 9, 16, 25]

    def test_lambda_with_filter(self):
        """Test lambda with filter function."""
        numbers = [1, 2, 3, 4, 5, 6]
        evens = list(filter(lambda x: x % 2 == 0, numbers))
        assert evens == [2, 4, 6]


class TestRecursion:
    """Test recursive functions."""

    def test_factorial(self):
        """Test factorial calculation with recursion."""
        def factorial(n: int) -> int:
            if n <= 1:
                return 1
            return n * factorial(n - 1)
        
        assert factorial(5) == 120
        assert factorial(3) == 6

    def test_fibonacci(self):
        """Test Fibonacci sequence with recursion."""
        def fibonacci(n: int) -> int:
            if n <= 1:
                return n
            return fibonacci(n - 1) + fibonacci(n - 2)
        
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8


class TestNestedFunctions:
    """Test functions defined inside functions."""

    def test_nested_function(self):
        """Test nested function definition."""
        def outer(x):
            def inner(y):
                return x + y
            return inner(5)
        
        result = outer(10)
        assert result == 15

    def test_closure(self):
        """Test closure capturing outer variable."""
        def make_multiplier(n):
            def multiplier(x):
                return x * n
            return multiplier
        
        double = make_multiplier(2)
        triple = make_multiplier(3)
        
        assert double(5) == 10
        assert triple(5) == 15
