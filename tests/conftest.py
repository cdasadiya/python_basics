"""Pytest configuration and fixtures for the test suite."""

import pytest
from io import StringIO
import sys
from pathlib import Path


@pytest.fixture
def capture_output():
    """Fixture to capture stdout during tests."""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    yield sys.stdout
    sys.stdout = old_stdout


@pytest.fixture
def sample_data():
    """Fixture providing sample data for tests."""
    return {
        'numbers': [1, 2, 3, 4, 5],
        'strings': ['apple', 'banana', 'orange'],
        'mixed': [1, 'two', 3.0, True, None],
        'marks': [90, 85, 78, 92, 88],
    }


@pytest.fixture
def temp_file(tmp_path):
    """Fixture providing a temporary file for file handling tests."""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Sample content\n")
    return test_file
